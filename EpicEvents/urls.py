from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from User.views import SignupViewset
from Client.views import ClientViewset
from Contract.views import ContractViewset

router = routers.SimpleRouter()

router.register('signup', SignupViewset, basename='signup')
router.register('clients', ClientViewset, basename="clients")

client_router = routers.NestedSimpleRouter(router, r'clients', lookup='client')

client_router.register(r'contract', ContractViewset, basename='contract')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('', include(client_router.urls)),
]
