from django.contrib.auth.decorators import login_required
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
    queryset = Car.objects.filter(rented=False)


class CarListView(ListView):
    model = Car
    template_name = "car/list_cars.html"
    context_object_name = "carros"


class RentListView(ListView):
    model = Rent
    template_name = "rent/list_rents.html"
    context_object_name = "alugueis"

    def get_queryset(self):
        return Rent.objects.filter(user=self.request.user,)


@login_required
def rent_car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    if request.method == 'POST':
        form = RentForm(request.POST)

        if form.is_valid():
            rent = form.save()
            return redirect(reverse_lazy("list_rents"))

    else:
        form = RentForm()
    return render(request, 'rent/create_rent.html', {'form': form, 'carro': car})
