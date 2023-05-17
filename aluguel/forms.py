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
                attrs={
                    'type': 'date', 'placeholder': 'dd/mm/YYYY'}
            )
        }
