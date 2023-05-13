from django.urls import path
from django.views.generic import TemplateView

from .views import ProfileDetailView, ProfileUpdateView, Registration

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path("sobrenos/", TemplateView.as_view(template_name="about.html"), name="about"),
    path("profile/", ProfileDetailView.as_view(), name="profile"),
    path("profile/edit", ProfileUpdateView.as_view(), name="edit_profile"),
    path("accounts/registration/", Registration.as_view(), name="registration")
]
