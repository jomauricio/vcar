from django.contrib.auth import get_user_model
from rest_framework import serializers

from core.models import Profile

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["name", "phone", "address", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:profile-detail", "lookup_field": "pk"},
        }
