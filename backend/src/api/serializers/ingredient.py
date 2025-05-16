from api.models.ingredient import Ingredient
from rest_framework import serializers


class IngredientSerializer(serializers.ModelSerializer):
    """
    Serializer for the Ingredient model.
    """

    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Ingredient
        fields = ["id", "name", "unit", "created_by"]
        read_only_fields = ["id"]
