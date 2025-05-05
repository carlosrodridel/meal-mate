import uuid

from api.models.ingredient import Ingredient
from api.models.recipe import Recipe
from django.db import models
from model_utils.models import TimeStampedModel


class RecipeIngredient(TimeStampedModel):
    """
    Model representing the relationship between a recipe and its ingredients.
    """

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="recipe_ingredients",
        verbose_name="recipe",
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name="recipe_ingredients",
        verbose_name="ingredient",
    )
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "recipe ingredient"
        verbose_name_plural = "recipe ingredients"
