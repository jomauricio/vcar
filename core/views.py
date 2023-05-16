from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import (CreateView, DetailView, TemplateView,
                                  UpdateView)
from sms import send_sms

from aluguel.models import Car

from .forms import ProfileForm, UserRegistrationForm
from .mixins import LoginRequiredAndIsOwnerMixin
from .models import Profile

User = get_user_model()


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["carros"] = Car.objects.all()[:3]
        return context


class ProfileDetailView(LoginRequiredAndIsOwnerMixin, DetailView):
    model = Profile
    template_name = "profile/profile.html"

    def get_object(self):
        return get_object_or_404(Profile, pk=self.request.user.profile.pk)


class ProfileUpdateView(LoginRequiredAndIsOwnerMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "profile/edit_profile.html"
    success_url = reverse_lazy("profile")

    def get_object(self):
        return get_object_or_404(Profile, pk=self.request.user.profile.pk)


class Registration(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy("profile")


class SettingsView(TemplateView):
    template_name = "profile/settings.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        phone_number = "+5586981103337"
        message = "Você acessou suas configurações as {}.".format(
            timezone.now())

        send_sms(message, None, [phone_number], fail_silently=False)
        return context
