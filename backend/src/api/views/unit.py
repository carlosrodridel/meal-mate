from api.models.unit import Unit
from api.serializers.unit import UnitSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class UnitViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows units to be viewed.
    """

    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [IsAuthenticated]
