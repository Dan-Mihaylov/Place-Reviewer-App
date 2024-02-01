from django import template

from TheReviewApp.review.models import Like
from django.db.models import Q


register = template.Library()


@register.filter
def get_type(value) -> str:
    return type(value)


@register.filter
def user_liked(review, user) -> bool:
    query = Q(user=user) & Q(review=review)
    return Like.objects.filter(query).exists()
