from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer

from django.http import HttpResponse


class UserViewSet(viewsets.ModelViewSet):
    """
    endpoint allow Users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    endpoint allows Groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


def index(request):
    return HttpResponse("hello kuba")



