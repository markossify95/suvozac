from rest_framework import generics
from rest_framework import viewsets
from core.models import CustomUser
from .serializers import UserSerializer
from .permissions import IsAuthenticatedOrCreate


class SignUp(generics.CreateAPIView):
    """
    A viewset for signing up.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrCreate,)


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
