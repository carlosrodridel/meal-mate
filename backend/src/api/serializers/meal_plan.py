from api.models.meal_plan import MealPlan, MealPlanEntry, MealPlanGroup
from rest_framework import serializers


class MealPlanSerializer(serializers.ModelSerializer):
    """
    Serializer for the Ingredient model.
    """

    class Meta:
        model = MealPlan
        fields = "__all__"
        read_only_fields = ["id", "name", "description", "created_by", "participants"]


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
        read_only_fields = ["id", "mealplan", "date_time", "recipe"]
