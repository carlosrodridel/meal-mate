from api.models.recipe import Recipe
from rest_framework import serializers


class RecipeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Recipe model.
    """

    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        help_text="The user who created the recipe.",
    )

    class Meta:
        model = Recipe
        fields = "__all__"
        read_only_fields = ["id", "created", "modified"]
