from api.models.ingredient import Ingredient
from api.serializers.ingredient import IngredientSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class IngredientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ingredients to be viewed or edited.
    """

    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Optionally restricts the returned ingredients to user created ones
        and global ingredients (created_by=None) by filtering against
        """
        queryset = Ingredient.objects.all()
        user = self.request.user
        queryset = queryset.filter(created_by=user) | queryset.filter(created_by=None)
        return queryset
