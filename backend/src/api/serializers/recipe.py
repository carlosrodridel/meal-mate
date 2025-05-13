from api.models.recipe import Recipe
from rest_framework import serializers


class RecipeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Recipe model.
    """

    class Meta:
        model = Recipe
        fields = "__all__"
        read_only_fields = ["id", "name", "description", "created_by"]
