from django.contrib import admin
from .models import FSSAIEntry, Review


@admin.register(FSSAIEntry)
class FSSAIEntryAdmin(admin.ModelAdmin):
	list_display = ('authorisation_name', 'fssai_code', 'number_of_orders', 'submitted_at')
	search_fields = ('authorisation_name', 'fssai_code')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
	list_display = ('name', 'entry', 'rating', 'created_at')
	list_filter = ('rating',)
