from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TableViewSet, CallServerViewSet, create_call_server


router = DefaultRouter()
router.register(r'tables', TableViewSet)
router.register(r'calls', CallServerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create-call/', create_call_server, name='create-call-server'),
]
