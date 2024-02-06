from django.contrib import admin

from TheReviewApp.accounts.models import UserInfo


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    pass

