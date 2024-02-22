from django.db import models
from django.contrib.auth.models import AbstractUser

class User (AbstractUser):

    AUTHOR = 'AUTHOR'
    READER = 'READER'
    ADMIN = 'ADMIN'

    ROLE_CHOICES = (

        (AUTHOR, 'AUTHOR'),
        (READER, 'READER'),
        (ADMIN, 'ADMIN')
    )
    profile_photo = models.ImageField()
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)
