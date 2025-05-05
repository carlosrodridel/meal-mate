import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class MealPlan(TimeStampedModel):
    """
    Model representing a meal plan.
    """

    name = models.CharField(_("name"), max_length=255, blank=False, null=False)
    description = models.TextField(_("description"), blank=True, null=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    created_by = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="meal_plans",
        verbose_name=_("created by"),
    )
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL, through="UserMealPlan", related_name="mealplans"
    )

    class Meta:
        verbose_name = _("meal plan")
        verbose_name_plural = _("meal plans")


class UserMealPlan(models.Model):
    ROLE_CHOICES = [
        ("owner", "Owner"),
        ("editor", "Editor"),
        ("viewer", "Viewer"),
    ]
    """
    Model representing a user in a meal plan.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_mealplans",
    )
    mealplan = models.ForeignKey(
        MealPlan, on_delete=models.CASCADE, related_name="user_mealplans"
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="viewer")
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "mealplan")

    def __str__(self):
        return f"{self.user} in {self.mealplan} as {self.role}"


class MealPlanEntry(models.Model):
    """
    Model representing an entry in a meal plan.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    meal_plan = models.ForeignKey(
        MealPlan, on_delete=models.CASCADE, related_name="entries"
    )
    recipe = models.ForeignKey(
        "Recipe", on_delete=models.CASCADE, related_name="meal_plan_entries"
    )
    date_time = models.DateTimeField(_("date and time"), blank=False, null=False)

    class Meta:
        unique_together = ("meal_plan", "recipe", "date_time")
