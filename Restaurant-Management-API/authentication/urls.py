from rest_framework.urls import path
from authentication import views

urlpatterns = [
    path("create/", views.CreateUserAPIView.as_view()),
    path("delete/", views.DeleteUserAPIView.as_view())
]
