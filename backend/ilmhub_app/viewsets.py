from .serializers import LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response
from rest_framework  import viewsets, status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.permissions import IsAuthenticated , AllowAny
from .models import User

class LoginViewSet(viewsets.ModelViewSet, TokenObtainPairView):
    """
    A viewset for viewing and editing user instances.

    :param viewsets: Viewset class
    :type viewsets: class
    :param TokenObtainPairView: TokenObtainPairView class
    :type TokenObtainPairView: class
    :return: The validated user data from the login attempt
    :rtype: Response
    """
    
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class RefreshTokenViewSet(viewsets.ModelViewSet, TokenRefreshView):
    """
    A viewset for viewing and editing user instances.

    :param viewsets: Viewset class
    :type viewsets: class
    :param TokenRefreshView: TokenRefreshView class
    :type TokenRefreshView: class
    :return: The validated user data from the refresh
    :rtype: Response
    """

    permissions_classes = [AllowAny]


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)