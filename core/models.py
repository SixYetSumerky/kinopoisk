from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    avatar=models.ImageField(upload_to='core/avatars/',null=True,blank=True)
    favorite_films=models.ManyToManyField('app.Movie')