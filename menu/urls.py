from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlatViewSet


router = DefaultRouter()
router.register(r'plats', PlatViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
