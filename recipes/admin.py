from django.contrib import admin

# Register your models here.
from .models import Recipe, Ingredient, RecipeIngredient

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    