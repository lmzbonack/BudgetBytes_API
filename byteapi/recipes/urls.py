from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'', views.RecipesViewSet, base_name='recipes')

urlpatterns = [
    url(r'^', include(router.urls)),
]