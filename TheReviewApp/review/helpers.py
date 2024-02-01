from django.contrib.auth.models import User
from django.db.models import Q

from TheReviewApp.review.models import Review, Like


def filter_reviews_by(request, place):
    request_options = {
        'time_a': place.reviews.all(),
        'time_d': place.reviews.order_by('-added_on'),
        'stars_a': place.reviews.order_by('stars'),
        'stars_d': place.reviews.order_by('-stars'),
    }

    reviews = request_options[request.GET.get('filter_by', 'time_d')]
    return reviews


def liked_already(user: User, review: Review) -> bool:
    query = Q(user=user) & Q(review=review)
    return Like.objects.filter(query).exists()


def like_review(user: User, review: Review) -> None:
    like = Like.objects.create(user=user, review=review)
    like.save()
    return


def dislike_review(user: User, review: Review) -> None:
    query = Q(user=user) & Q(review=review)
    like_object = Like.objects.get(query)
    like_object.delete()
    return

