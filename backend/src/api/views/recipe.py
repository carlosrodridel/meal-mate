from api.models.recipe import Recipe
from api.serializers.recipe import RecipeSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows recipes to be viewed or edited.
    """

    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Optionally restricts the returned recipes to user created ones
        and global recipes (created_by=None) by filtering against
        """
        queryset = Recipe.objects.all()
        user = self.request.user
        queryset = queryset.filter(created_by=user) | queryset.filter(created_by=None)
        return queryset
