from api.models.ingredient import Ingredient
from api.models.recipe import Recipe
from api.models.recipe_ingredient import RecipeIngredient
from api.serializers.recipe_ingredient import RecipeIngredientSerializer
from rest_framework import serializers


class RecipeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Recipe model.
    """

    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        help_text="The user who created the recipe.",
    )
    ingredients = RecipeIngredientSerializer(many=True, source="recipe_ingredients")

    class Meta:
        model = Recipe
        fields = "__all__"
        read_only_fields = ["id", "created_by", "ingredients"]

    def create(self, validated_data):
        ingredients_data = validated_data.pop("recipe_ingredients", [])
        recipe = Recipe.objects.create(**validated_data)
        # link existing ingredients
        for entry in ingredients_data:
            ing = Ingredient.objects.get(pk=entry["ingredient_id"])
            RecipeIngredient.objects.create(
                recipe=recipe, ingredient=ing, quantity=entry["quantity"]
            )
        return recipe
