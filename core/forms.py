from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField, ModelForm

from .models import Profile

User = get_user_model()


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ("user", "width_avatar", "height_avatar")


class UserRegistrationForm(UserCreationForm):
    email = EmailField(label='Email', required=True,
                       help_text="Email pessoal.")

    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = User
