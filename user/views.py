from rest_framework import generics
# from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        """
        Retrieve and return authenticated user
        """
        return self.request.user
