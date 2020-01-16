from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth


# # Create your models here.

class Profile(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    ceo = models.BooleanField(default=False)

