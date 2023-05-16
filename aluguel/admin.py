from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin

from .models import Car, Rent


@admin.register(Car)
class CarAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ("plate", "model", "brand", "year")
    list_filter = ("year",)
    search_fields = ("plate", "model",)
    readonly_fields = ["width_image", "height_image", "rented"]


@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_display = ("rental_number", "user",)
    list_filter = ("rent_date", "return_date", "user",)
    search_fields = ("rental_number", "user",)
    autocomplete_fields = ["car", "user"]
