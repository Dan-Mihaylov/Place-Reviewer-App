def filter_reviews_by(request, place):
    request_options = {
        'time_a': place.reviews.all(),
        'time_d': place.reviews.order_by('-added_on'),
        'stars_a': place.reviews.order_by('stars'),
        'stars_d': place.reviews.order_by('-stars'),
    }

    reviews = request_options[request.GET.get('filter_by', 'time_d')]
    return reviews

