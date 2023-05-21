from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import DetailView, ListView
from sms import send_sms

from .forms import RentForm
from .models import Car, Rent

# Create your views here.


class CarDetailView(DetailView):
    model = Car
    template_name = "car/detail_car.html"
    context_object_name = "carro"


class RentDetailView(DetailView):
    model = Rent
    template_name = "rent/recive_rent.html"
    context_object_name = "aluguel"


class CarListView(ListView):
    model = Car
    template_name = "car/list_cars.html"
    context_object_name = "carros"
    queryset = Car.objects.filter(rented=False)


class RentListView(LoginRequiredMixin, ListView):
    model = Rent
    template_name = "rent/list_rents.html"
    context_object_name = "alugueis"

    def get_queryset(self):
        return Rent.objects.filter(user=self.request.user).order_by("-rent_date").order_by("concluded")


class AttendantRentListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Rent
    template_name = "rent/attendant_list_rents.html"
    context_object_name = "alugueis"
    permission_required = "aluguel"
    ordering = "rent_date"
    queryset = Rent.objects.filter(concluded=False)


@login_required
def rent_car(request, car_plate):
    car = get_object_or_404(Car, pk=car_plate)

    if car.rented:
        messages.error(
            request, "O carro de placa {} já está alucado.".format(car.plate.upper()))
        return redirect(reverse_lazy("list_cars"))

    else:
        if request.method == 'POST':
            form = RentForm(request.POST)
            form.instance.car = car
            form.instance.user = request.user
            if form.is_valid():
                form.instance.car.rented = True
                form.instance.car.save()
                form.save()
                messages.success(
                    request, "O carro de placa {} foi alugado com sucesso.".format(car.plate.upper()))
                phone_number = "+5586981103337"  # request.user.profile
                message = "O carro de placa {} foi alugado com sucesso em {}".format(car.plate.upper(),
                                                                                     timezone.now().strftime("%d/%m%Y, %H:%M:%S"))
                send_sms(message, None, [phone_number], fail_silently=False)
                return redirect(reverse_lazy("list_rents"))
            else:
                form = RentForm()
                messages.error(
                    request, "Não é possível alugar um veículo em datas passadas.")
                return render(request, 'rent/create_rent.html', {'form': form, 'carro': car})
        else:
            form = RentForm()
        return render(request, 'rent/create_rent.html', {'form': form, 'carro': car})


@login_required
@permission_required("aluguel")
def rent_recive_car(request, rental_number):
    rent = get_object_or_404(Rent, rental_number=rental_number)
    rent.car.rented = False
    rent.car.save()
    rent.concluded = True
    rent.return_date = timezone.now().date()
    rent.save()
    messages.success(
        request, "O carro de placa {} foi devolvido com sucesso.".format(rent.car.plate.upper()))
    phone_number = "+5586981103337"  # request.user.profile
    message = "O carro de placa {} foi devolvido com sucesso em {}".format(rent.car.plate.upper(
    ),                                                                      timezone.now().strftime("%d/%m%Y, %H:%M:%S"))
    send_sms(message, None, [phone_number], fail_silently=False)
    return redirect(reverse_lazy("attendant_list_rents"))
