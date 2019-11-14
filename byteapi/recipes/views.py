"""Recipe endpoint views"""

from rest_framework import generics, filters

from .models import Recipe
from .serializers import RecipeSerializer

class RecipesViewSet(generics.ListCreateAPIView):
    """View set for Pending Documents"""
    search_fields = ['name', 'ingredients']
    filter_backends = (filters.SearchFilter,)
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
