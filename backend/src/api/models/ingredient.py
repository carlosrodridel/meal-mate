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
    quantity = models.CharField(max_length=255, blank=True, null=True)
    unit = models.ForeignKey(
        "Unit",
        on_delete=models.CASCADE,
        related_name="ingredients",
        verbose_name=_("unit"),
    )
    recipe = models.ForeignKey(
        "Recipe",
        on_delete=models.CASCADE,
        related_name="ingredients",
        verbose_name=_("recipe"),
    )

    class Meta:
        verbose_name = _("ingredient")
        verbose_name_plural = _("ingredients")
