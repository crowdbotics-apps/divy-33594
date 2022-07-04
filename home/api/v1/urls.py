from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    AccountsViewSet,
    DividendsViewSet,
    DripViewSet,
    HoldingsViewSet,
    HoldingValueViewSet,
)

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("holdings", HoldingsViewSet)
router.register("accounts", AccountsViewSet)
router.register("drip", DripViewSet)
router.register("holdingvalue", HoldingValueViewSet)
router.register("dividends", DividendsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
