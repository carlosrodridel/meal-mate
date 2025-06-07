from api.models.ingredient import Ingredient
from api.models.recipe import Recipe
from api.models.recipe_ingredient import RecipeIngredient
from api.models.unit import Unit
from api.serializers.recipe_ingredient import (
    RecipeIngredientCreateSerializer,
    RecipeIngredientSerializer,
)
from rest_framework import serializers


class RecipeListSerializer(serializers.ModelSerializer):
    """
    Serializer for listing recipes.
    """

    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        help_text="The user who created the recipe.",
    )

    class Meta:
        model = Recipe
        fields = ["id", "name", "description", "created_by", "ingredients"]
        read_only_fields = ["id", "created_by"]


class RecipeCreateSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        help_text="The user who created the recipe.",
    )
    ingredient_lines = serializers.SerializerMethodField(read_only=True)
    ingredients = RecipeIngredientCreateSerializer(many=True, write_only=True)

    class Meta:
        model = Recipe
        fields = (
            "id",
            "name",
            "created_by",
            "description",
            "ingredients",  # ⬅ write‐only
            "ingredient_lines",  # ⬅ read‐only
        )

    def get_ingredient_lines(self, recipe_obj):
        lines = recipe_obj.ingredient_lines.select_related("ingredient").all()
        return [
            {
                "id": line.ingredient.id,
                "name": line.ingredient.name,
                "quantity": line.quantity,
                "unit": line.ingredient.unit.id if line.ingredient.unit else None,
            }
            for line in lines
        ]

    def create(self, validated_data):
        ingredients_data = validated_data.pop("ingredients", [])

        entries = []

        for ing_line in ingredients_data:
            quantity = ing_line["quantity"]

            if "id" in ing_line:
                print(f"Processing ingredient {ing_line}")
                try:
                    ingredient = Ingredient.objects.get(
                        pk=ing_line["id"],
                        created_by__in=[None, validated_data["created_by"]],
                    )
                except Ingredient.DoesNotExist:
                    raise serializers.ValidationError(
                        f"Ingredient with id={ing_line['id']} not found."
                    )

            else:
                ingredient_name = ing_line["name"].strip()
                try:
                    unit = Unit.objects.get(pk=ing_line["unit"])
                except Unit.DoesNotExist:
                    raise serializers.ValidationError(
                        f"Unit with id={ing_line['unit']} not found."
                    )

                ingredient, _ = Ingredient.objects.get_or_create(
                    name=ingredient_name,
                    unit=unit,
                    created_by=validated_data["created_by"],
                )

            entries.append((ingredient, quantity))

        recipe = Recipe.objects.create(
            name=validated_data["name"],
            description=validated_data.get("description", ""),
            created_by=validated_data["created_by"],
        )

        for ingredient, quantity in entries:
            RecipeIngredient.objects.create(
                recipe=recipe,
                ingredient=ingredient,
                quantity=quantity,
            )

        return recipe


# class RecipeSerializer(serializers.ModelSerializer):
#     """
#     Serializer for the Recipe model.
#     """

#     created_by = serializers.HiddenField(
#         default=serializers.CurrentUserDefault(),
#         help_text="The user who created the recipe.",
#     )
#     ingredients = RecipeIngredientSerializer(many=True, source="recipe_ingredients")

#     class Meta:
#         model = Recipe
#         fields = "__all__"
#         read_only_fields = ["id", "created_by", "ingredients"]

#     def create(self, validated_data):
#         ingredients_data = validated_data.pop("recipe_ingredients", [])
#         recipe = Recipe.objects.create(**validated_data)
#         # link existing ingredients
#         for entry in ingredients_data:
#             ing = Ingredient.objects.get(pk=entry["ingredient_id"])
#             RecipeIngredient.objects.create(
#                 recipe=recipe, ingredient=ing, quantity=entry["quantity"]
#             )
#         return recipe
