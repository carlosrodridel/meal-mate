from api.models.recipe_ingredient import RecipeIngredient
from rest_framework import serializers


class RecipeIngredientSerializer(serializers.ModelSerializer):
    """
    Serializer for the RecipeIngredient model.
    """

    class Meta:
        model = RecipeIngredient
        fields = "__all__"
        read_only_fields = ["id", "recipe", "ingredient", "quantity"]
