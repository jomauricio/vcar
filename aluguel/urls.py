from django.urls import path
from django.views.generic import TemplateView

from .views import CarDetailView, CarListView

urlpatterns = [
    path("car/", CarListView.as_view(), name="list_cars"),
    path("car/<str:pk>/", CarDetailView.as_view(), name="detail_car"),
    # path("profile/edit/", ProfileUpdateView.as_view(), name="edit_profile"),
    # path("profile/settings/", SettingsView.as_view(), name="settings"),
]
