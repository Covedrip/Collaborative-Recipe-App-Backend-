from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)  # Comma-separated or a JSONField
    instructions = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='recipes/images/', null=True, blank=True)
    dietary_tags = models.CharField(max_length=255, null=True, blank=True)  # E.g., "vegan,gluten-free"
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class RecipeCollaboration(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='collaborations')
    suggested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    suggestion_text = models.TextField()
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"Suggestion by {self.suggested_by} for {self.recipe.title}"
    
    

    