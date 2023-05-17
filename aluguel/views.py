from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
# from django.utils import timezone
from django.views.generic import DetailView, ListView

from .forms import RentForm
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
    queryset = Car.objects.filter(rented=False)


class RentListView(LoginRequiredMixin, ListView):
    model = Rent
    template_name = "rent/list_rents.html"
    context_object_name = "alugueis"

    def get_queryset(self):
        return Rent.objects.filter(user=self.request.user,)


@login_required
def rent_car(request, car_plate):
    car = get_object_or_404(Car, pk=car_plate)

    if car.rented:
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
                return redirect(reverse_lazy("list_rents"))
        else:
            form = RentForm()
        return render(request, 'rent/create_rent.html', {'form': form, 'carro': car})
