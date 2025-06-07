from api.models.recipe import Recipe
from api.permissions import IsCreatorOrReadOnly
from api.serializers.recipe import RecipeCreateSerializer, RecipeListSerializer
from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated


class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows recipes to be viewed or edited.
    """

    permission_classes = [IsAuthenticated, IsCreatorOrReadOnly]
    queryset = Recipe.objects.all().prefetch_related("ingredient_lines__ingredient")

    def get_serializer_class(self):
        """
        Return the appropriate serializer class based on the action.
        """
        # if self.action in ["list", "retrieve"]:
        #     print(f"Using RecipeListSerializer for action: {self.action}")
        #     return RecipeListSerializer
        return RecipeCreateSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned recipes to user created ones
        and global recipes (created_by=None) by filtering against
        """
        queryset = Recipe.objects.all()
        user = self.request.user
        queryset = queryset.filter(created_by=user) | queryset.filter(created_by=None)
        return queryset
