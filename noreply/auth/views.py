from rest_framework_simplejwt.views import TokenObtainPairView

from auth.serializers import ClientAuthSerializer


class ClientAuthView(TokenObtainPairView):
    serializer_class = ClientAuthSerializer
    