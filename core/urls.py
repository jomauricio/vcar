from django.urls import path
from django.views.generic import TemplateView

from .views import (IndexView, ProfileDetailView, ProfileUpdateView,
                    Registration, SettingsView)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("sobrenos/", TemplateView.as_view(template_name="about.html"), name="about"),
    path("profile/", ProfileDetailView.as_view(), name="profile"),
    path("profile/edit/", ProfileUpdateView.as_view(), name="edit_profile"),
    path("profile/settings/", SettingsView.as_view(), name="settings"),
    path("accounts/registration/", Registration.as_view(), name="registration")
]
