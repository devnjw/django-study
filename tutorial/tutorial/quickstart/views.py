from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer

from django.contrib.auth.mixins import LoginRequiredMixin

class UserViewSet(viewsets.ModelViewSet, LoginRequiredMixin):
    """
    사용자(user)를 보거나 편집하는 API
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    그룹(group)을 보거나 편집하는 API
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer