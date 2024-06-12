from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    sender = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='sender')
    receiver = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='receiver')
    content = models.JSONField(default=dict)