from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth


# # Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=6, null=True)
    ceo = models.BooleanField(default=False)

