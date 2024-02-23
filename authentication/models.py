from django.db import models
from django.contrib.auth.models import AbstractUser, Group


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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.role == self.AUTHOR:
            group = Group.objects.get(name='authors')
            group.user_set.add(self)
        elif self.role == self.READER:
            group = Group.objects.get(name='readers')
            group.user_set.add(self)
        elif self.role == self.ADMIN:
            Group.objects.get(name='readers').user_set.add(self)
