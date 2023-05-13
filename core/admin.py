from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ("id", "user", "name", "avatar")
    list_filter = ("user",)
    search_fields = ("name",)
    readonly_fields = ["width_avatar", "height_avatar"]
