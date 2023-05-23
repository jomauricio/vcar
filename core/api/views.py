from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from core.models import Profile

from .serializers import ProfileSerializer

User = get_user_model()


class ProfileViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    # def get_queryset(self, *args, **kwargs):
    #     assert isinstance(self.request.profile.id, int)
    #     return self.queryset.filter(id=self.request.profile.id)

    # @action(detail=False)
    # def me(self, pk):
    #     serializer = ProfileSerializer()
    #     return Response(status=status.HTTP_200_OK, data=serializer.data)
