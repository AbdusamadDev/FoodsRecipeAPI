from rest_framework.authtoken.views import Token
from rest_framework import generics, status
from django.contrib.auth.models import User
from authentication import serializers
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class CreateUserAPIView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
    model = User

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.validated_data["username"]
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            self.model.objects.create_user(username=username, email=email, password=password)
            user = authenticate(request=request, username=username, email=email, password=password)
            login(request=request, user=user)
            user = self.model.objects.get(pk=request.user.id)
            token = Token.objects.create(user=user)
            return Response(
                data={"token": token.key}, 
                status=status.HTTP_201_CREATED)
        return Response(data={"msg": "Data not validated"})
        

class DeleteUserAPIView(generics.DestroyAPIView):
    model = User
    lookup_field = "pk"
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user_id = request.user.id
        self.model.objects.get(pk=user_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
