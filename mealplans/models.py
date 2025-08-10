from django.db import models
from django.conf import settings
from recipes.models import Recipe, Ingredient
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Meal(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='meals'
    )

    name = models.CharField(max_length=50, choices=[
        ('breakfast', 'breakfast'), ('lunch', 'lunch'),
        ('dinner', 'dinner'), ('snack', 'snack'),
    ])
    ''
    def __str__(self):
        return f"{self.user.username} - {self.name}"
    
class MealPlan(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='meal_plans'
    )
    name = models.CharField(max_length=100)

    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    days = models.ManyToManyField(
        MealPlanDay,
        through='PlanDay',
        related_name='meal_plans'
    )

    def __str__(self):
        return f"{self.name} for {self.user.username}"

class MealPlanDay(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='meal_plan_days'
    )
    meal_plan = models.ForeignKey(
        MealPlan,
        on_delete=models.CASCADE,
        related_name='days'
    )
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('meal_plan', 'day')

    def __str__(self):
        return f"{self.day} of {self.meal_plan.name}"

class Meal(models.Model):
    name = models.CharField(max_length=50, unique=True, choices=[
        ('breakfast', 'Сніданок'), ('lunch', 'Обід'),
        ('dinner', 'Вечеря'), ('snack', 'Перекус'),
    ])
    meal_plan_day = models.ForeignKey(
        MealPlanDay,
        on_delete=models.CASCADE,
        related_name='meals'
    )

    def __str__(self):
        return f"{self.name} on {self.meal_plan_day.day}"

class MealItem(models.Model):
    meal = models.ForeignKey(
        Meal,
        on_delete=models.CASCADE,
        related_name='items'
    )
    servings = models.IntegerField(default=1)

    # Generic Foreign Key для зв'язку з Recipe або Ingredient
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"{self.servings} servings of {self.content_object} in {self.meal.name}"