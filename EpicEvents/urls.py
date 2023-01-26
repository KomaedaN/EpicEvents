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
router.register('contract', ContractViewset, basename='contract')
router.register('event', EventViewset, basename='event')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
