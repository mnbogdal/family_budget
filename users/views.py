from django.contrib.auth.models import User

from rest_framework import viewsets
from .serializers import UserSerializer


class UsersView(viewsets.ModelViewSet):
    """
    Endpoint for returning User data.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
