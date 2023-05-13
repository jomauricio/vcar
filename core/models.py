from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse_lazy
from sorl.thumbnail import ImageField

# Create your models here.

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Usuário")
    name = models.CharField("Nome", blank=True, max_length=255)
    phone = models.CharField("Telefone", blank=True, max_length=20)
    mobile = models.CharField("Celular", blank=True, max_length=20)
    address = models.CharField("Celular", blank=True, max_length=255)
    bio = models.TextField("Bio", blank=True)
    avatar = ImageField(
        blank=True,
        upload_to="avatars",
        verbose_name="Avatar",
        width_field="width_avatar",
        height_field="height_avatar",
    )
    width_avatar = models.PositiveIntegerField(null=True, blank=True)
    height_avatar = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("profile")

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"
