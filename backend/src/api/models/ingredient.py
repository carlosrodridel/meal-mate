import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class Ingredient(TimeStampedModel):
    """
    Model representing an ingredient.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    unit = models.ForeignKey(
        "Unit",
        on_delete=models.CASCADE,
        related_name="ingredients",
        verbose_name=_("unit"),
    )
    created_by = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="created_ingredients",
        verbose_name=_("created by"),
    )

    class Meta:
        verbose_name = _("ingredient")
        verbose_name_plural = _("ingredients")
