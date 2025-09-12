from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from auth.models import Client


class ClientAuthSerializer(serializers.Serializer):
    """Сериализатор получения токенов"""
    
    client_id = serializers.CharField()
    client_secret = serializers.CharField()

    def validate(self, attrs):
        client_id = attrs.get("client_id")
        client_secret = attrs.get("client_secret")

        try:
            client = Client.objects.get(client_id=client_id, client_secret=client_secret, is_active=True)
        except Client.DoesNotExist:
            raise AuthenticationFailed("Invalid client_id or secret")
        
        refresh = RefreshToken.for_user(client)

        return {
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        }
