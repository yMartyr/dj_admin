from django.db import models

# Create your models here.

class UserInfo(models.Model):
    uname=models.CharField(max_length=32)
    email=models.CharField(max_length=32)
