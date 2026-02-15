from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeviceViewSet

router = DefaultRouter()
router.register(r'', DeviceViewSet, basename='device')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]