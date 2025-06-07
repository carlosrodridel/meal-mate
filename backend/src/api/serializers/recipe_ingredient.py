from api.models.ingredient import Ingredient
from api.models.recipe_ingredient import RecipeIngredient
from api.serializers.ingredient import IngredientSerializer
from rest_framework import serializers


class RecipeIngredientCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating RecipeIngredient instances.
    """

    id = serializers.UUIDField(required=False, write_only=True)
    name = serializers.CharField(
        required=False, write_only=True, help_text="Name of the ingredient"
    )
    unit = serializers.UUIDField(
        required=False, write_only=True, help_text="Unit of the ingredient"
    )

    class Meta:
        model = RecipeIngredient
        fields = ["id", "name", "quantity", "unit"]
        read_only_fields = ["id"]

    def validate_id(self, value):
        user = self.context["request"].user
        # ensure the ingredient exists and is visible to this user
        if not Ingredient.objects.filter(
            id=value, created_by__in=[None, user]
        ).exists():
            print(f"Ingredient with id {value} not found for user {user}.")
            raise serializers.ValidationError("Ingredient not found.")
        return value

    def validate(self, attrs):
        has_id = "id" in attrs
        has_name = "name" in attrs
        has_unit = "unit" in attrs

        if has_id and (has_name or has_unit):
            raise serializers.ValidationError(
                "Cannot provide 'id' with 'name' or 'unit'."
            )

        if not has_id and not (has_name and has_unit):
            raise serializers.ValidationError(
                "Must provide either 'id' or both 'name' and 'unit'."
            )
        return attrs


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
