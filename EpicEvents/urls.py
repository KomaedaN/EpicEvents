from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from User.views import SignupViewset
from Client.views import ClientViewset
from Contract.views import ContractViewset
from Event.views import EventViewset, EventStatusViewset

router = routers.SimpleRouter()

router.register('signup', SignupViewset, basename='signup')
router.register('clients', ClientViewset, basename="clients")
router.register('event_status', EventStatusViewset, basename='event_status')

client_router = routers.NestedSimpleRouter(router, r'clients', lookup='client')
client_router.register(r'contract', ContractViewset, basename='contract')

contract_router = routers.NestedSimpleRouter(client_router, r'contract', lookup='contract')
contract_router.register(r'event', EventViewset, basename='event')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('', include(client_router.urls)),
    path('', include(contract_router.urls)),
]
