"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from api.views import ingredient as ingredient_views
from api.views import meal_plan as meal_plan_views
from api.views import recipe as recipe_views
from api.views import recipe_ingredient as recipe_ingredient_views
from api.views import unit as unit_views
from api.views import user as user_views
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r"users", user_views.UserViewSet)
router.register(r"groups", user_views.GroupViewSet)

router.register(
    r"ingredients", ingredient_views.IngredientViewSet, basename="ingredient"
)
router.register(r"units", unit_views.UnitViewSet, basename="unit")
router.register(r"meal-plans", meal_plan_views.MealPlanViewSet, basename="meal-plan")
# router.register(
#     r"meal-plan-groups",
#     meal_plan_views.MealPlanGroupViewSet,
#     basename="meal-plan-group",
# )
router.register(
    r"meal-plan-entries",
    meal_plan_views.MealPlanEntryViewSet,
    basename="meal-plan-entry",
)
router.register(r"recipes", recipe_views.RecipeViewSet, basename="recipe")
router.register(
    r"recipe-ingredients",
    recipe_ingredient_views.RecipeIngredientViewSet,
    basename="recipe-ingredient",
)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
