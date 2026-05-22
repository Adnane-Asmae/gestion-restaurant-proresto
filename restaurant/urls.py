
from django.urls import path
from . import views

urlpatterns = [
    # Tables endpoints
    path('tables/', views.tables_list, name='tables-list'),
    path('tables/<int:pk>/', views.tables_detail, name='tables-detail'),
    path('tables/create/', views.tables_create, name='tables-create'),
    path('tables/<int:pk>/update/', views.tables_update, name='tables-update'),
    path('tables/<int:pk>/delete/', views.tables_delete, name='tables-delete'),
    path('tables/<int:pk>/regenerate_qr/', views.tables_regenerate_qr, name='tables-regenerate-qr'),
    
    # Calls endpoints
    path('calls/', views.calls_list, name='calls-list'),
    path('calls/<int:pk>/resolve/', views.calls_resolve, name='calls-resolve'),
    path('create-call/', views.create_call_server, name='create-call-server'),
]

