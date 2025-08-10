from django.db import models

# Create your models here.

class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recipes')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    calories = models.IntegerField(null=True, blank=True)
    image_path = models.ImageField(upload_to='recipes/images/', blank=True, null=True)
    
