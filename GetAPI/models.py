from django.db import models

# Create your models here.

class userinfo(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()