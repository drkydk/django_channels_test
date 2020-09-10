from django.db import models
from django.contrib.auth.models import User


class Channel(models.Model):
    room_name = models.CharField(max_length=64, default='')
    seen_by = models.CharField(max_length=64, default='')


class Message(models.Model):
    room = models.ForeignKey(Channel, on_delete=models.DO_NOTHING)
    content = models.CharField(max_length=512)
    sender = models.CharField(max_length=32, default='')
    recipient = models.CharField(max_length=32, default='')
    # sender = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='sender')
    # recipient = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='recipient')
    timestamp = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)
