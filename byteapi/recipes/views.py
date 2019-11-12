"""Recipe endpoint views"""

from rest_framework import viewsets

from .models import Recipe
from .serializers import RecipeSerializer

class RecipesViewSet(viewsets.ModelViewSet):
    """View set for Pending Documents"""

    serializer_class = RecipeSerializer

    def get_queryset(self):
        return Recipe.objects.all().order_by('modified')
