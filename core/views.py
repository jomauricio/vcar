from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .forms import ProfileForm, UserRegistrationForm
from .mixins import LoginRequiredAndIsOwnerMixin
from .models import Profile

User = get_user_model()


class ProfileDetailView(LoginRequiredAndIsOwnerMixin, DetailView):
    model = Profile
    template_name = "profile/profile.html"

    def get_object(self):
        return get_object_or_404(Profile, pk=self.request.user.profile.pk)


class ProfileUpdateView(LoginRequiredAndIsOwnerMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "profile/edit_profile.html"

    # def get_success_url(self):
    #     return reverse_lazy("profile")

    def get_object(self):
        return get_object_or_404(Profile, pk=self.request.user.profile.pk)


class Registration(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy("profile")
