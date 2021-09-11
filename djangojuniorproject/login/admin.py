from django.contrib import admin
from login.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("pk", "user")
    list_display_links = ("pk", "user")
    search_fields = ("user__username",)

    readonly_fields = ("user",)
