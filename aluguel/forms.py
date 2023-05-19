from django.forms import DateInput, ModelForm, ValidationError
from django.utils import timezone

from .models import Car, Rent


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = "__all__"


class RentForm(ModelForm):
    class Meta:
        model = Rent
        fields = ("rent_date",)
        # exclude = ("user", "car", "return_date", "concluded")
        widgets = {
            'rent_date': DateInput(
                attrs={'type': 'date'}
            )
        }

    def clean_rent_date(self):
        rent_date = self.cleaned_data['rent_date']

        if rent_date < timezone.now().date():
            raise ValidationError(
                "Não é possível alugar um veículo em datas passadas.")

        return rent_date


class AttendantRentForm(ModelForm):
    class Meta:
        model = Rent
        fields = "__all__"
        exclude = ("user", "car", "rent_date", "concluded")
        widgets = {
            'return_date': DateInput(
                attrs={
                    'type': 'date'}
            )
        }

    def clean_return_date(self):
        return_date = self.cleaned_data['return_date']

        if return_date > timezone.now().date():
            raise ValidationError(
                "Não é possível devolver um veículo em datas futuras.")

        return return_date
