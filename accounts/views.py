from django.contrib.auth import authenticate
from django.utils import timezone
from rest_framework import status, generics, exceptions, response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import LoginSerializer, UserSerializer, RegistrationSerializer


class LoginView(generics.GenericAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if not user:
            raise exceptions.AuthenticationFailed()

        user.last_login = timezone.now()
        user.save()

        refresh = RefreshToken.for_user(user)
        data = {
            "user": UserSerializer(instance=user, context={"request": request}).data,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        return response.Response(data=data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    authentication_classes = ()
    permission_classes = ()

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        response.delete_cookie('jwt_refresh')
        response.delete_cookie('jwt_access')
        return response


class RegistrationView(generics.GenericAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        data = {
            "user": UserSerializer(instance=user, context={"request": request}).data,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        return response.Response(data=data, status=status.HTTP_201_CREATED)
