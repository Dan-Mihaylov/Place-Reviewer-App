from django.urls import path, include
from TheReviewApp.accounts import views


urlpatterns = (
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('account/', include(
        [
            path('', views.account_info, name='account-info'),
            path('edit/', views.edit_account, name='edit-account'),
            path('delete/', views.delete_account, name='delete-account'),
        ]
    )
         )
)
