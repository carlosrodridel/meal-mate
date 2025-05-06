import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Unit(models.Model):
    """
    Model representing a unit of measurement.
    """

    class Category(models.TextChoices):
        WEIGHT = "weight", "Weight"
        VOLUME = "volume", "Volume"
        COUNT = "count", "Count"
        LENGTH = "length", "Length"
        TIME = "time", "Time"
        TEMP = "temp", "Temperature"
        AREA = "area", "Area"
        HYBRID = "hybrid", "Volume-Weight Hybrid"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True, blank=False, null=False)
    abbreviation = models.CharField(max_length=10, unique=True, blank=False, null=False)
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.WEIGHT,
        blank=False,
        null=False,
    )
    conversion_factor = models.FloatField(
        default=1.0,
        blank=False,
        null=False,
        help_text=_("Conversion factor to base unit"),
    )

    class Meta:
        verbose_name = _("unit")
        verbose_name_plural = _("units")
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.abbreviation})"
