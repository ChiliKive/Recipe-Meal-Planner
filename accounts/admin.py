from django.contrib import admin
from .models import UserProfile

# Реєструємо модель UserProfile для адмін-панелі.
admin.site.register(UserProfile)