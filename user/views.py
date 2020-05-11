from rest_framework import generics
# from rest_framework.settings import api_settings
from rest_framework.permissions import AllowAny, IsAuthenticated
from user.serializers import UserSerializer
from rest_framework.response import Response


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

class HelloView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        content = {
            "title": "The Basics - Networking",
            "description": "Your app fetched this from a remote endpoint",
            "movies": [
                { "title": "Star Wars", "releaseYear": "1977"},
                { "title": "Back to the Future", "releaseYear": "1985"},
                { "title": "The Matrix", "releaseYear": "1999"},
                { "title": "Inception", "releaseYear": "2010"},
                { "title": "Interstellar", "releaseYear": "2014"}	
            ]
        }
        return Response(content)