from rest_framework import serializers
from .models import Recipe, RecipeCollaboration, User
from rest_framework.authtoken.views import Token


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        # fields = ['title', 'description', 'ingredients', 'instructions', 'image', 'dietary_tags', 'created_by', 'created_at', 'updated_at']
        fields = '__all__'
        
        

class RecipeCollaborationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeCollaboration
        # field = ['recipe', 'suggested_by', 'suggestion_text', 'is_accepted ']
        fields = '__all__'
    
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        
        extra_kwargs = {'password':{
            'write_only':True,
            'required':True
         } }
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user