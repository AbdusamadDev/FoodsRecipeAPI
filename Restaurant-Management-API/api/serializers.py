from rest_framework.serializers import Serializer
from api.models import RecipesNameModel, RecipesModel
from rest_framework import serializers
from rest_framework.response import Response


class RecipesSerializer(Serializer):
    name_model = RecipesNameModel
    model = RecipesModel

    food_name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=6000, required=False)
    recipe = serializers.JSONField()

    def get_object_id(self, name):
        query = self.name_model.objects.filter(food_name=name).first()
        if query is None:
            return None
        return query

