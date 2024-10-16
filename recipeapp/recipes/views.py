# from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Recipe, RecipeCollaboration
from .serializers import UserSerializer, RecipeSerializer, RecipeCollaborationSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts  import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import APIView
from rest_framework import generics, mixins 
# Create your views here.


#Views for user creation
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    


# class RecipeViewSet(viewsets.ModelViewSet):
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer
#     permission_classes = [IsAuthenticated]


# class RecipeCollaborationViewSet(viewsets.ModelViewSet):
#     queryset = RecipeCollaboration.objects.all()
#     serializer_class = RecipeCollaborationSerializer
#     permission_classes = [IsAuthenticated]
    
#View recipes
'''
class CreateRecipeView(CreateAPIView):
    permission_classes = []
    serializer_class = RecipeSerializer

class RecipeViewSet(viewsets.ViewSet):
    
    def list(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = RecipeSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        queryset = Recipe.objects.all()
        recipes = get_object_or_404(queryset, pk=pk)
        serializer = RecipeSerializer(recipes)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        recipes = Recipe.objects.get(pk=pk)
        serializer = RecipeSerializer(recipes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        recipes = Recipe.objects.get(pk=pk)
        recipes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class RecipeCollaborationViewSet(viewsets.ViewSet):
    
    def list(self, request):
        recipes = RecipeCollaboration.objects.all()
        serializer = RecipeCollaborationSerializer(recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        queryset = RecipeCollaboration.objects.all()
        recipes = get_object_or_404(queryset, pk=pk)
        serializer = RecipeCollaborationSerializer(recipes)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        recipes = RecipeCollaboration.objects.get(pk=pk)
        
        serializer = RecipeCollaborationSerializer(recipes)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        '''
  
  
'''      
class RecipeList(APIView):
    
    def get(self, request):
        recipes= Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RecipeDetail(APIView):
    
    def get_recipe(self, pk):
        try:
            return Recipe.objects.get(pk=pk)
        
        except Recipe.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get(self, request, pk):
        recipe = self.get_recipe(pk)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        serializer = RecipeSerializer(data=request.data, pk=pk)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        recipe = self.get_recipe(pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Collaboration(APIView):
    
    def get(self, request):
        collab = RecipeCollaboration.objects.all()
        serializer = RecipeCollaborationSerializer(collab, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = RecipeCollaborationSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CollaborationDetail(APIView):
    
    def get_collab(self, pk):
        try:
            return RecipeCollaboration.objects.get(pk=pk)
        
        except RecipeCollaboration.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        
    def get(self,request, pk):
        collab = self.get_collab(pk)
        serializer = RecipeCollaborationSerializer(collab)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request,pk):
        serializer = RecipeCollaborationSerializer(data=request.data, pk=pk)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        collab = self.get_collab(pk)
        collab.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        '''

class RecipeList(generics.ListAPIView, generics.CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class RecipeDetail(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]
    
    lookup_field = 'id'
    
    def get(self, request, id):
        return self.retrieve(request, id)
    
    def put(self, request, id):
        return self.update(request, id=id)
    
    def delete(self, request, id):
        return self.destroy(request, id=id)
    
class Collaboration(generics.CreateAPIView, generics.ListAPIView):
    queryset = RecipeCollaboration.objects.all()
    serializer_class = RecipeCollaborationSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class CollaborationDetail(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = RecipeCollaboration.objects.all()
    serializer_class = RecipeCollaborationSerializer
    permission_classes = [IsAuthenticated]
    
    lookup_field = 'id'
    
    def get(self, request, id):
        return self.retrieve(request,  id=id)
    
    def put(self, request, id):
        return self.update(request, id=id)
    
    def delete(self, request, id):
        return self.destroy(request, id)
        