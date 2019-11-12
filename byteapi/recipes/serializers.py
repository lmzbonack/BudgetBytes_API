"""Pending Documents Endpoint Serializer"""
from rest_framework import serializers

from .models import Recipe 

class RecipeSerializer(serializers.ModelSerializer):
    """Recipe Serializer"""

    class Meta:
        model = Recipe
        fields = ('author', 'cook_time', 'created', 'image_url', 'ingredients', 'instructions', 'keywords',
        'name', 'prep_time', 'modified')