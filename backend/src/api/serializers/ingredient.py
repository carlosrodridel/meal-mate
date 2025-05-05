from api.models.ingredient import Ingredient
from api.models.unit import Unit
from rest_framework import serializers


class IngredientSerializer(serializers.ModelSerializer):
    """
    Serializer for the Ingredient model.
    """

    class Meta:
        model = Ingredient
        fields = "__all__"
        read_only_fields = ["id", "name", "unit"]
