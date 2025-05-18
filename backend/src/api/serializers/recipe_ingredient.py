from api.models.ingredient import Ingredient
from api.models.recipe_ingredient import RecipeIngredient
from api.serializers.ingredient import IngredientSerializer
from rest_framework import serializers


class RecipeIngredientSerializer(serializers.ModelSerializer):
    """
    Serializer for the RecipeIngredient model.
    """

    ingredient_id = serializers.UUIDField(write_only=True)
    ingredient = IngredientSerializer(read_only=True)

    class Meta:
        model = RecipeIngredient
        fields = ["ingredient_id", "quantity", "ingredient"]

    def validate_ingredient_id(self, value):
        user = self.context["request"].user
        # ensure the ingredient exists and is visible to this user
        if not Ingredient.objects.filter(
            id=value, created_by__in=[None, user]
        ).exists():
            raise serializers.ValidationError("Ingredient not found.")
        return value
