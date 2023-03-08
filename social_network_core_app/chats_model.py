from django.db import models
from django.contrib.auth.models import User

class ChatRoom(models.Model):
    name = models.CharField(max_length=255)

class Message(models.Model):
    room = models.ForeignKey(ChatRoom,related_name='chat_roomms', on_delete=models.CASCADE)
    sender = models.ForeignKey(User,related_name='sender_name', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
