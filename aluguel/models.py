from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse_lazy
from django_extensions.db.fields import RandomCharField
from django_extensions.db.models import TimeStampedModel
from sorl.thumbnail import ImageField

# Create your models here.
User = get_user_model()


class Car(TimeStampedModel):
    plate = models.CharField("Placa", primary_key=True, max_length=7,
                             help_text="Escreva a placa no formato: XXXXXXX")
    brand = models.CharField("Marca", max_length=50)
    model = models.CharField("Modelo", max_length=50)
    year = models.CharField("Ano", max_length=4)
    rented = models.BooleanField("Alugado")
    image = ImageField(
        blank=True,
        upload_to="cars",
        verbose_name="Imagem",
        width_field="width_image",
        height_field="height_image",
    )
    width_image = models.PositiveIntegerField(null=True, blank=True)
    height_image = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return "{} - {} - {}".format(self.plate, self.model, self.brand)

    def get_absolute_url(self):
        return reverse_lazy("cars", plate=self.plate)

    class Meta:
        verbose_name = "Carro"
        verbose_name_plural = "Carros"


class Rent(TimeStampedModel):

    rental_number = RandomCharField(
        "Codigo", length=6, lowercase=True,  unique=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE,
                            verbose_name="Carro", related_name="car_rents")
    rent_date = models.DateField("Data de aluguel")
    return_date = models.DateField(
        "Data de devolução", null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Cliente", related_name="user_rents")

    def __str__(self):
        if self.user.profile.name:
            return "{} - {}".format(self.rental_number, self.user.profile.name)
        else:
            return "{} - {}".format(self.rental_number, self.user.email)

    def get_absolute_url(self):
        return reverse_lazy("rent", rental_number=self.rental_number)

    class Meta:
        verbose_name = "Aluguel"
        verbose_name_plural = "Alugueis"
