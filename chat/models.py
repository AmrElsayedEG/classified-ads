from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class chat(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='first')
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name='second')
    message = models.TextField(max_length=500)
    date_sent = models.DateTimeField(auto_now_add=True, blank=True)
