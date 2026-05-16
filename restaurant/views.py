from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Table, CallServer
from .serializers import TableSerializer, CallServerSerializer
from django.utils import timezone


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context
    
    @action(detail=True, methods=['post'])
    def regenerate_qr(self, request, pk=None):
        table = self.get_object()
        table.regenerate_qr_code()
        serializer = self.get_serializer(table)
        return Response(serializer.data)


class CallServerViewSet(viewsets.ModelViewSet):
    queryset = CallServer.objects.all().order_by('-date_creation')
    serializer_class = CallServerSerializer
    
    @action(detail=True, methods=['post'])
    def resolve(self, request, pk=None):
        call = self.get_object()
        call.statut = 'resolved'
        call.date_resolution = timezone.now()
        call.save()
        serializer = self.get_serializer(call)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def create_call_server(request):
    table_id = request.data.get('table_id')
    try:
        table = Table.objects.get(id=table_id)
        call = CallServer.objects.create(table=table)
        serializer = CallServerSerializer(call)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Table.DoesNotExist:
        return Response({'error': 'Table not found'}, status=status.HTTP_404_NOT_FOUND)

