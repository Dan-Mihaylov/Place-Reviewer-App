from django.shortcuts import render, get_object_or_404

from .models import Place


def index(request):
    places = Place.objects.all()

    return render(request, template_name='review/index.html', context={'places': places})


def view_reviews(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    reviews = place.reviews.all()
    context = {
        'place': place,
        'reviews': reviews,
        'rating': round(place.total_stars()['average'], 2),
    }

    return render(request, template_name='review/place_reviews.html', context=context)
