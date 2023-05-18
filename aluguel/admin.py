from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin

from .models import Car, Rent


@admin.action(description="Liberar carros para aluguel")
def make_published(modeladmin, request, queryset):
    queryset.update(rented=False)


@admin.register(Car)
class CarAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ("plate", "model", "brand", "year", "rented", "image")
    list_filter = ("year",)
    search_fields = ("plate", "model",)
    readonly_fields = ["width_image", "height_image"]
    actions = [make_published]


@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_display = ("rental_number", "user", "car")
    list_filter = ("rent_date", "return_date", "user",)
    search_fields = ("rental_number", "user",)
    autocomplete_fields = ["car", "user"]
