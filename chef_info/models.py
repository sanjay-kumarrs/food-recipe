from django.db import models
from django.contrib.auth.models import User
from modules.models import recipes
from modules.models import chef

# Create your models here.
class feedBack(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField()

   





