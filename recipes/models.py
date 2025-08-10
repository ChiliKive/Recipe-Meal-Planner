from django.db import models
from django.conf import settings

# Create your models here.

class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recipes')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    instructions = models.TextField(blank=True)

    calories = models.IntegerField(null=True, blank=True)
    
    protein = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    carbohydrates = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    fats = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    fiber = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    image_path = models.ImageField(upload_to='recipes/images/', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=50, choices=[
        ('g', 'grams'),
        ('ml', 'milliliters'),
        ('kg', 'kilograms'),
        ('oz', 'ounces'),
        ('lb', 'pounds'),
        ('l', 'liters'),
    ])
    calories_per_unit = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    protein_per_unit = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    carbohydrates_per_unit = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    fats_per_unit = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    fiber_per_unit = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='recipe_ingredients')
    quantity = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('recipe', 'ingredient')

    