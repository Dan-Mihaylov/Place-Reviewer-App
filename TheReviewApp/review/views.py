from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from TheReviewApp.review.helpers import filter_reviews_by
from TheReviewApp.review.models import Place
from TheReviewApp.review.forms import PlaceAddForm, ReviewWriteForm, FilterForm


def index(request):

    context = {
        'places': Place.objects.all(),
        'user': request.user if request.user.id is not None else 'blank',
    }

    print(request.user.username)

    return render(request, template_name='review/index.html', context=context)


def view_reviews(request, place_id):

    place = get_object_or_404(Place, id=place_id)
    reviews = filter_reviews_by(request, place)

    context = {
        'place': place,
        'reviews': reviews,
        'rating': round(place.total_stars()['average'], 2) if place.reviews.all() else 'No Rating',
        'form': FilterForm()
    }

    return render(request, template_name='review/place_reviews.html', context=context)


@login_required(login_url='login')
def place_add(request):

    if request.method == 'POST':
        form = PlaceAddForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            # place = form.save(commit=False)
            # place.user = request.user
            # place.save()

            return redirect('index')
    form = PlaceAddForm(request.user)   # In the form I have created, __init__ takes the user
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
