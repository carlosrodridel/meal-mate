import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class Recipe(TimeStampedModel):
    """
    Model representing a recipe.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="recipes",
        verbose_name=_("created by"),
    )

    class Meta:
        verbose_name = _("recipe")
        verbose_name_plural = _("recipes")
