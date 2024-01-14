from django.shortcuts import render, get_object_or_404, redirect

from .models import Place
from .forms import PlaceAddForm, ReviewWriteForm, FilterForm


def index(request):
    places = Place.objects.all()

    return render(request, template_name='review/index.html', context={'places': places})


def view_reviews(request, place_id):
    print(request.GET)
    place = get_object_or_404(Place, id=place_id)
    reviews = place.reviews.all()
    context = {
        'place': place,
        'reviews': reviews,
        'rating': round(place.total_stars()['average'], 2) if place.reviews.all() else 'No Rating',
        'form': FilterForm()
    }

    return render(request, template_name='review/place_reviews.html', context=context)


def place_add(request):

    if request.method == 'POST':
        form = PlaceAddForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    form = PlaceAddForm()

    return render(request, template_name='review/place_add.html', context={'form': form})


def write_review(request, place_id: int):
    place = get_object_or_404(Place, id=place_id)
    context = {
        'place': place,
    }

    if request.method == 'POST':
        form = ReviewWriteForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.place = place
            review.save()
            return redirect('reviews', place_id)

    context['form'] = ReviewWriteForm()

    return render(request, template_name='review/place_write_review.html', context=context)


