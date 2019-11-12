from django.contrib import admin

from recipes.models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):

    """Admin Panel configuration"""

    fieldsets = (
        ('Recipe Data', {
            'fields': [('name'),
                       ('ingredients'),
                       ('instructions'),
                       ('prep_time'),
                       ('cook_time'),
                       ('image_url'),
                       ('keywords'),
                       ('author'),]
        }),
    )
    readonly_fields = ('created', 'modified',)
    list_display = ('ingredients', 'instructions',)
    list_filter = ('name', 'ingredients', 'instructions', 'prep_time', 'cook_time', 'keywords', 'author')
