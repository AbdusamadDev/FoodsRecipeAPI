from django.db import models

class RecipesNameModel(models.Model):
    food_name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["food_name"], name="unique_food_name")
        ]
        indexes = [
            models.Index(fields=["id"])
        ]

class RecipesModel(models.Model):
    food_name = models.ForeignKey(to="api.RecipesNameModel", on_delete=models.CASCADE)
    ingredient = models.TextField(max_length=6000, blank=False, unique=False)
    quantity = models.CharField(max_length=200, blank=True, default="Quantity not provided")
    date_created = models.DateTimeField(auto_now_add=True)
