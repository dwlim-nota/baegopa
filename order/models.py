from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)