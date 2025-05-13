from api.models.recipe_ingredient import RecipeIngredient
from api.serializers.recipe_ingredient import RecipeIngredientSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class RecipeIngredientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows recipe ingredients to be viewed or edited.
    """

    serializer_class = RecipeIngredientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        queryset = RecipeIngredient.objects.all()
        user = self.request.user
        queryset = queryset.filter(recipe__created_by=user) | queryset.filter(
            recipe__created_by=None
        )
        return queryset
