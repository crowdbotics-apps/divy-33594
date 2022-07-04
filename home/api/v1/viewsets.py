from rest_framework import viewsets
from home.models import Accounts, Dividends, Drip, Holdings, HoldingValue
from .serializers import (
    AccountsSerializer,
    DividendsSerializer,
    DripSerializer,
    HoldingsSerializer,
    HoldingValueSerializer,
)
from rest_framework import authentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from home.api.v1.serializers import (
    SignupSerializer,
    UserSerializer,
)


class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ["post"]


class LoginViewSet(ViewSet):
    """Based on rest_framework.authtoken.views.ObtainAuthToken"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({"token": token.key, "user": user_serializer.data})


class HoldingsViewSet(viewsets.ModelViewSet):
    serializer_class = HoldingsSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Holdings.objects.all()


class AccountsViewSet(viewsets.ModelViewSet):
    serializer_class = AccountsSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Accounts.objects.all()


class DripViewSet(viewsets.ModelViewSet):
    serializer_class = DripSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Drip.objects.all()


class HoldingValueViewSet(viewsets.ModelViewSet):
    serializer_class = HoldingValueSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = HoldingValue.objects.all()


class DividendsViewSet(viewsets.ModelViewSet):
    serializer_class = DividendsSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Dividends.objects.all()
