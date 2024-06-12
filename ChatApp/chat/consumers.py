import json
from channels.generic.websocket import AsyncWebsocketConsumer 
from asgiref.sync import async_to_sync
from django.contrib.auth.models import User
from time import sleep
import datetime
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from chat.models import Chat
User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        print ("connecting ....")
        print(f"user ==================> {self.scope['user']}")
        await self.accept() 
        await self.channel_layer.group_add(f"mychat_app_{self.scope['user']}", self.channel_name)
         
         
    async def disconnect(self, close_code): 
        pass
    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data = json.loads(text_data)
        await self.channel_layer.group_send(
            f"mychat_app_{text_data['user']}",
            {
                'type':'send.msg',
                'msg':text_data['msg']
            }
            )
        await self.save_chat(text_data)
    @database_sync_to_async   
    def save_chat(self,text_data):
        receiver = User.objects.get(username=text_data['user'])
        chats, created = Chat.objects.get_or_create(sender=self.scope['user'], receiver=receiver)
        # If the object was just created, initialize the 'content' field as an empty dictionary
        if created:
            chats.content = {}
        chats.content[str(datetime.datetime.now())+"1"] = {'user': 'sender', 'msg': text_data['msg']}
        chats.save()
        chats, created = Chat.objects.get_or_create(sender=receiver, receiver=self.scope['user'])
        # If the object was just created, initialize the 'content' field as an empty dictionary
        if created:
            chats.content = {}
        chats.content[str(datetime.datetime.now())+"2"] = {'user': receiver.username, 'msg': text_data['msg']}
        chats.save()
    async def send_msg(self,event):
        # print(event['msg'])
        await  self.send(event['msg'])
