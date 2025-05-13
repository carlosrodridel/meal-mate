from api.models.unit import Unit
from rest_framework import serializers


class UnitSerializer(serializers.ModelSerializer):
    """
    Serializer for the Unit model.
    """

    class Meta:
        model = Unit
        fields = "__all__"
