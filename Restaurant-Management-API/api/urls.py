from rest_framework.urls import path
from api import views

urlpatterns = [
    path("recipes/", views.RecipesAPIView.as_view()),
    path("recipes/<int:pk>/", views.RecipesAPIView.as_view()),
    path("delete/<int:pk>", views.DeleteRecipeAPIView.as_view()),
    path("details/<int:pk>/", views.RecipesDetailAPIView.as_view()),
]