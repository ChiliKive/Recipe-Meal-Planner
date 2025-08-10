from django.db import models

# Create your models here.

class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 