from django.urls import path
from TheReviewApp.review.views import index, view_reviews, place_add, write_review, edit_place, delete_place


urlpatterns = (
    path('', index, name='index'),
    path('<int:place_id>/reviews/<int:review_id>/', view_reviews, name='reviews_with_likes'),
    path('<int:place_id>/reviews/', view_reviews, name='reviews'),
    path('add/', place_add, name='place_add'),
    path('<int:place_id>/reviews/write', write_review, name='write_review'),
    path('edit_place/<int:place_id>', edit_place, name='edit_place'),
    path('delete_place/<int:place_id>', delete_place, name='delete_place'),
)

