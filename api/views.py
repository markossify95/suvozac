from rest_framework import generics
from rest_framework import viewsets
from core.models import CustomUser
from .serializers import UserSerializer
from .permissions import IsAuthenticatedOrCreate
from rest_framework import permissions
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope


class SignUp(generics.CreateAPIView):
    """
    A viewset for signing up.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrCreate,)


"""
class UserViewSet(viewsets.ModelViewSet):
    """  # A viewset for viewing and editing user instances.
"""
serializer_class = UserSerializer
queryset = CustomUser.objects.all()
"""


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
