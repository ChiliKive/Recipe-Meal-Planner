from django.db import models

# Create your models here.

class Recipe(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)