from django.urls import path
from TheReviewApp.accounts.views import register_page, login_page, logout_page


urlpatterns = (
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
)

