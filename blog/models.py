from django.db import models
from PIL import Image
from authentication.models import User
from django.conf import settings

class Blog (models.Model):
    image = models.ImageField(null=True)
    caption = models.CharField(max_length=30, blank=True)
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=5000)
    contributors = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    IMAGE_MAX_SIZE = (800, 800)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
