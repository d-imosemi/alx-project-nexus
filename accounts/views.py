from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import LogoutSerializer, RegisterSerializer, UserSerializer
from rest_framework import generics, permissions, status
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


# Logout (Blacklist token)
class LogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """
        Logout the user by blacklisting their refresh token.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Get refresh token from validated data
        refresh_token = serializer.validated_data.get("refresh")
        token = RefreshToken(refresh_token)
        token.blacklist()  

        return Response(
            {"message": "Logged out successfully"}, 
            status=status.HTTP_205_RESET_CONTENT
        )


# Get/Update User Profile
class UserDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user