from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from TheReviewApp.review.helpers import (
    filter_reviews_by, like_review, liked_already, dislike_review
)
from TheReviewApp.review.models import Place, Review
from TheReviewApp.review.forms import PlaceAddForm, ReviewWriteForm, FilterForm, EditPlaceForm


def index(request):

    context = {
        'places': Place.objects.all(),
        'user': request.user if request.user.id is not None else 'blank',
    }

    print(request.user.username)

    return render(request, template_name='review/index.html', context=context)


def delete_place(request, place_id):

    place = get_object_or_404(Place, id=place_id)

    if request.user != place.user:
        return render(request, 'cheeky_monkey.html')

    place.delete()
    return redirect('index')


def view_reviews(request, place_id, review_id=None):

    place = get_object_or_404(Place, id=place_id)
    reviews = filter_reviews_by(request, place)
    if review_id is not None:
        review = reviews.get(id=review_id)
        user = request.user
        dislike_review(user, review) if liked_already(user, review) else like_review(user, review)

    context = {
        'place': place,
        'reviews': reviews,
        'rating': round(place.total_stars()['average'], 2) if place.reviews.all() else 'No Rating',
        'form': FilterForm(),
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


def edit_place(request, place_id):

    place = get_object_or_404(Place, id=place_id)
    # Check if someone unauthorised is trying to edit the place info.
    if place.user.id != request.user.id:
        return redirect('index')

    form = EditPlaceForm(instance=place)    # request.user

    if request.method == 'POST':
        form = EditPlaceForm(request.POST, instance=place)  # request.user

        print(f"Post: {request.POST}")

        if form.is_valid():

            # Here you edit the instance of place that we have with the valid form-cleaned-data, then we save
            # the instance of place, without creating new one. If we use `` form.save() `` we will create a new
            # instance of place, with duplicate information.

            place.name = form.cleaned_data['name']
            place.location = form.cleaned_data['location']
            place.description = form.cleaned_data['description']
            place.photo = form.cleaned_data['photo']
            place.user = request.user
            place.save()
            return redirect('index')

    context = {
        'place': place,
        'form': form,
    }

    return render(request, 'review/edit_place.html', context=context)
