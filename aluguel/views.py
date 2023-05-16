# from django.shortcuts import render
from django.views.generic import (CreateView, DetailView, ListView,
                                  TemplateView, UpdateView)

from .models import Car, Rent

# Create your views here.


class CarDetailView(DetailView):
    model = Car
    template_name = "car/detail_car.html"
    context_object_name = "carro"


class CarListView(ListView):
    model = Car
    template_name = "car/list_cars.html"
    context_object_name = "carros"


# class ProfileUpdateView(LoginRequiredAndIsOwnerMixin, UpdateView):
#     model = Profile
#     form_class = ProfileForm
#     template_name = "profile/edit_profile.html"
#     success_url = reverse_lazy("profile")

#     def get_object(self):
#         return get_object_or_404(Profile, pk=self.request.user.profile.pk)


# class SettingsView(TemplateView):
#     template_name = "profile/settings.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         phone_number = "+5586981103337"
#         message = "Você acessou suas configurações as {}.".format(
#             timezone.now())

#         send_sms(message, None, [phone_number], fail_silently=False)
#         return context
