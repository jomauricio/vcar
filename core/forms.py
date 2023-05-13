from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ("user", "width_avatar", "height_avatar")


class UserRegistrationForm(UserCreationForm):
    pass
