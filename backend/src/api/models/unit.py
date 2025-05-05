import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Unit(models.Model):
    """
    Model representing a unit of measurement.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    symbol = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name = _("unit")
        verbose_name_plural = _("units")
        ordering = ["name"]
