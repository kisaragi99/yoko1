from django.contrib import admin

# Register your models here.

from .models import Category, Title

admin.site.register(Category)
admin.site.register(Title)