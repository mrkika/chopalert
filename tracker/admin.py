from django.contrib import admin
from .models import FoodSpot  # make sure the model name matches


@admin.register(FoodSpot)
class FoodSpotAdmin(admin.ModelAdmin):
    list_display = ('food_type', 'description',
                    'posted_at')  # customize as needed
    search_fields = ('description', 'food_type')
    list_filter = ('food_type', 'posted_at')
