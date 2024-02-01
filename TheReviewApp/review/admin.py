from django.contrib import admin
from .models import Review, Place, Like


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'stars']


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'review_username', 'short_description']

    @staticmethod
    def short_description(obj):
        description = obj.review.comment
        return description[:35] + '...'

    @staticmethod
    def review_username(obj):
        return obj.review.username
