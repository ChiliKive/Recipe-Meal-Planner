from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # password
    # email
    # first_name
    # last_name
    # ...
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    pass
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    age = models.PositiveIntegerField(null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    weight = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[
        ('male', 'Male'),
        ('female', 'Female')
    ])
    activity_level = models.CharField(max_length=20, choices=[
        ('sedentary', 'Sedentary'),
        ('lightly_active', 'Lightly Active'),
        ('moderately_active', 'Moderately Active'),
        ('very_active', 'Very Active'),
        ('extra_active', 'Extra Active')
    ], default='sedentary')
    daily_calories = models.PositiveIntegerField(null=True, blank=True)
    daily_protein = models.PositiveIntegerField(null=True, blank=True)
    daily_carbs = models.PositiveIntegerField(null=True, blank=True)
    daily_fats = models.PositiveIntegerField(null=True, blank=True)
    daily_fiber = models.PositiveIntegerField(null=True, blank=True)
    goal = models.CharField(max_length=20, choices=[
        ('loss', 'Mass Loss'),
        ('gain', 'Mass Gain'),
        ('maintenance', 'Maintenance')
    ], default='maintenance')