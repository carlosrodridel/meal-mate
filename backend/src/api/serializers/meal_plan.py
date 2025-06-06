from api.models.meal_plan import MealPlan, MealPlanEntry, MealPlanGroup
from rest_framework import serializers


class MealPlanSerializer(serializers.ModelSerializer):
    """
    Serializer for the Ingredient model.
    """

    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        help_text="The user who created the meal plan.",
    )

    class Meta:
        model = MealPlan
        fields = "__all__"
        read_only_fields = ["id", "created_by", "participants"]


class MealPlanGroupSerializer(serializers.ModelSerializer):
    """
    Serializer for the MealPlanGroup model.
    """

    class Meta:
        model = MealPlanGroup
        fields = "__all__"
        read_only_fields = ["id", "user", "mealplan", "role", "joined_at"]


class MealPlanEntrySerializer(serializers.ModelSerializer):
    """
    Serializer for the MealPlanEntry model.
    """

    class Meta:
        model = MealPlanEntry
        fields = "__all__"
        read_only_fields = ["id"]
