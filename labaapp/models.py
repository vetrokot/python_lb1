from datetime import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Message(models.Model):
    content = models.CharField(max_length=500,default='')
    timestamp = models.DateTimeField( default=datetime.now() )
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='msg_sender')
 
    def __str__(self):
        return self.sender.username + ": "+self.content
    class Meta:
        unique_together = ['content']
       
 
# Create your models here.
