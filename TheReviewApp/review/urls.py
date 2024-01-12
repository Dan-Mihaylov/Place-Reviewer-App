from django.urls import path
from .views import index, view_reviews


urlpatterns = (
    path('', index, name='index'),
    path('<int:place_id>/reviews', view_reviews, name='reviews')
)

