from datetime import date

from django.core.exceptions import ValidationError
from django.forms import DateInput, ModelForm

from .models import Car, Rent


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = "__all__"


class RentForm(ModelForm):
    class Meta:
        model = Rent
        fields = "__all__"
        exclude = ("user", "car", "return_date")
        widgets = {
            'rent_date': DateInput(
                attrs={'type': 'date'}
            )
        }

        def clean_rent_date(self):
            rent_date = self.cleaned_data['rent_date']
            if rent_date < date.today():
                raise ValidationError(
                    "Não é possível alugar um veículo em datas passadas.", code="invalid_rent_date")

            return rent_date


class AttendantRentForm(ModelForm):
    class Meta:
        model = Rent
        fields = "__all__"
        exclude = ("user", "car", "rent_date")
        widgets = {
            'return_date': DateInput(
                attrs={
                    'type': 'date'}
            )
        }

        def clean_return_date(self):
            return_date = self.cleaned_data['return_date']
            if return_date > date.today():
                print("Deu erro")
                raise ValidationError(
                    "Não é possível devolver um veículo em datas futuras.", code="invalid_return_date")
            else:
                print("Deu certo")
                return return_date
