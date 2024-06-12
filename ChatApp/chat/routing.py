from django.urls import path , include
from .consumers import ChatConsumer
from django.urls import re_path

websocket_urlpatterns = [
    path("ws/wsc/" , ChatConsumer.as_asgi()), 
] 
