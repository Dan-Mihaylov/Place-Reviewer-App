from django.contrib.auth.models import User

from TheReviewApp.review.models import Review


def filter_reviews_by(request, place):
    request_options = {
        'time_a': place.reviews.all(),
        'time_d': place.reviews.order_by('-added_on'),
        'stars_a': place.reviews.order_by('stars'),
        'stars_d': place.reviews.order_by('-stars'),
    }

    reviews = request_options[request.GET.get('filter_by', 'time_d')]
    return reviews


def get_reviews_with_user_likes(request, reviews):
    user_id = request.user.id
    result = []
    for review in reviews:
        if review.user_likes.filter(id=user_id).exists():
            result.append(review.id)
    return result


def liked_already(user: User, review: Review):
    return review.user_likes.filter(id=user.id).exists()


def like_review(user: User, review: Review):
    review.add_user(user)


def dislike_review(user: User, review: Review):
    review.user_likes.remove(user)
