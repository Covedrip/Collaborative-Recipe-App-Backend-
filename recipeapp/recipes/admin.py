from django.contrib import admin
from .models import Recipe, RecipeCollaboration

# Register your models here.
admin.site.register(Recipe)
admin.site.register(RecipeCollaboration)