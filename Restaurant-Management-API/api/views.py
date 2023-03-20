from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, DestroyAPIView
from api import models, serializers
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.status import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication

# Create view, get list, delete row.
class RecipesAPIView(ListCreateAPIView):
    serializer_class = serializers.RecipesSerializer
    queryset = models.RecipesNameModel.objects.all()
    name_model = models.RecipesNameModel
    recipe_model = models.RecipesModel
    authentication_classes = [TokenAuthentication]
    permission_classes=[IsAuthenticated, IsAdminUser]

    def get_query_by_fk(self, pk):
        model_list = self.recipe_model.objects.filter(food_name=pk)
        return model_list.values_list("ingredient", "quantity")

    def list(self, request, *args, **kwargs):
        context = self.get_queryset().values_list()
        data = []
        for recipe in context:
            pk = recipe[0]
            ing = [{"ing": i[0], "qua": i[1]} for i in self.get_query_by_fk(pk=pk)]
            data.append(
                {
                    "recipe_name": recipe[1], 
                    "image": recipe[-3],
                    "description": recipe[-1],
                    "ingredients": ing
                }
            )
        return Response(data=data)          

    def get_queryset(self):
        query = self.name_model.objects.all()
        return query

    def create(self, request, *args, **kwargs):
        serializer = serializers.RecipesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                food_name = serializer.validated_data["food_name"]
                recipe_body = serializer.validated_data["recipe"]
                try:
                    name_model = models.RecipesNameModel(food_name=food_name)
                    name_model.save()
                    del serializer.validated_data["food_name"]
                except IntegrityError as error:
                    print(error.args)
                finally:
                    try:
                        food_id = serializer.get_object_id(name=food_name)
                        if food_id is None:
                            return Response(data={"msg": "food_id is None"}, status=HTTP_400_BAD_REQUEST)
                        print(recipe_body)
                        for query in recipe_body:
                            body_model = models.RecipesModel(
                                food_name=food_id, ingredient=query.get("ing"), quantity=query.get("qua"))
                            body_model.save()
                        return Response(
                            data={"msg": "Success data has been successfully created!"}, 
                            status=HTTP_201_CREATED
                        )
                    except AttributeError:
                        return Response(
                            data={"msg": "Data validation failed!"})
                    except IntegrityError:
                        return Response(
                            data={"msg": "Please enter json looks like this: {'ing': 'ingredient', 'qua': 'quantity'}"})
            except KeyError as k:
                return Response(data={"msg": str(k)}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response(data={"msg": "Invalid data provided"})


class DeleteRecipeAPIView(DestroyAPIView):
    queryset = models.RecipesNameModel.objects.all()
    name_model = models.RecipesNameModel
    authentication_classes = [TokenAuthentication]
    permission_classes=[IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        query = self.name_model.objects.all()
        return query

    def destroy(self, request, pk, *args, **kwargs):
        try:
            self.get_queryset().get(id=pk).delete()
            return Response(status=HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response(
                data={"msg": f"Data not found with id: {pk}"}, status=HTTP_404_NOT_FOUND)

class RecipesDetailAPIView(RetrieveAPIView):
    queryset = models.RecipesModel.objects.all()
    serializer_class = serializers.RecipesSerializer
    model = models.RecipesNameModel
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self, pk):
        if pk is None:
            return None
        object = self.queryset.filter(food_name=pk).values_list("ingredient", "quantity")
        object = [{"ing": index[0], "qua": index[1]} for index in object]
        return object

    def get(self, request,  pk, *args, **kwargs):
        print(request.user.is_authenticated)
        food_data = self.model.objects.filter(pk=pk).values_list("food_name", "image_link", "description")
        context = {
            "food_name": food_data[0], 
            "description": food_data[1], 
            "image_link": food_data[-1], 
            "ingredient": self.get_queryset(pk=pk)
        }
        if not self.get_queryset(pk=pk):
            return Response(data={"msg": "Data Not Found"}, status=HTTP_404_NOT_FOUND)
        return Response(data=context, status=HTTP_200_OK)
