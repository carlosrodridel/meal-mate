from api.models.unit import Unit
from api.serializers.unit import UnitSerializer
from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS, IsAdminUser, IsAuthenticated


class UnitViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows units to be viewed.
    """

    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

    # permission_classes = [IsAuthenticated]
    def get_permissions(self):
        """
        - If the HTTP method is “safe” (GET, HEAD, OPTIONS): require IsAuthenticated.
        - Otherwise: require IsAdminUser.
        """
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated()]
        return [IsAdminUser()]
