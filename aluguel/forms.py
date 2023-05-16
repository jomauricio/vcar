from django.forms import ModelForm

from .models import Car, Rent


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = "__all__"


class RentForm(ModelForm):
    class Meta:
        model = Rent
        fields = "__all__"
