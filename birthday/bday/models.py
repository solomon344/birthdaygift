from django.db import models

# Create your models here.

class images(models.Model):
    picture = models.ImageField(upload_to="media")

class wishes(models.Model):
    wish = models.CharField(max_length=100000)
    