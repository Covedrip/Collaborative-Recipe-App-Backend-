# from .views import RecipeViewSet, RecipeCollaborationViewSet, UserViewSet, CreateRecipeView
from .views import RecipeList,RecipeDetail, Collaboration, CollaborationDetail
from django.urls import path, include
from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='users')
# router.register(r'recipes', RecipeViewSet, basename='recipes')
# router.register(r'collaborations', RecipeCollaborationViewSet, basename='collaborations')

# urlpatterns = [
#     path('api/', include(router.urls)),
   
# ]

urlpatterns = [
    path('recipes/', RecipeList.as_view()),
    path('recipes/<int:id>/', RecipeDetail.as_view()),
    path('collaborations/', Collaboration.as_view()),
    path('collaborations<int:id>/', CollaborationDetail.as_view())
]





