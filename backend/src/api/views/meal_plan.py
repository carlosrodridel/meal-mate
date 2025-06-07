from api.models.meal_plan import MealPlan, MealPlanEntry, MealPlanGroup
from api.serializers.meal_plan import (  # MealPlanGroupSerializer,
    MealPlanEntrySerializer,
    MealPlanSerializer,
)
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class MealPlanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows units to be viewed.
    """

    serializer_class = MealPlanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MealPlan.objects.filter(created_by=self.request.user)


# class MealPlanGroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows units to be viewed.
#     """

#     serializer_class = MealPlanGroupSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return MealPlanGroup.objects.filter(user=self.request.user)


class MealPlanEntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows units to be viewed.
    """

    serializer_class = MealPlanEntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MealPlanEntry.objects.filter(mealplan__created_by=self.request.user)
