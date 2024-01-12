from django.contrib import admin
from .models import Review, Place


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'stars']



@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location']
