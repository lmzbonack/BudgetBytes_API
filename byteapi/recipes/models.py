from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.

class Recipe(TimeStampedModel):
    """Fields for recipe model"""
    name = models.CharField(max_length=30,
                            primary_key=True)
    ingredients = models.TextField(null=True)
    instructions = models.TextField(null=True)
    prep_time = models.CharField(null=True,
                                 max_length=10)
    cook_time = models.CharField(null=True,
                                 max_length=10)
    image_url = models.CharField(null=True,
                                 max_length=255)
    keywords = models.TextField(null=True)
    author = models.CharField(null=True,
                             max_length=100)

    def __str__(self):
        return self.name