from rest_framework import viewsets,status
from .models import Person
from persons.serializers import PersonSerializer
from rest_framework.response import Response
import datetime
from django_filters.rest_framework import DjangoFilterBackend
from persons.utils.filters import PersonFilter
from rest_framework.filters import OrderingFilter,SearchFilter

# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.filter(
        deleted_at__isnull = True
    )
    serializer_class = PersonSerializer
    filter_backends = (OrderingFilter,DjangoFilterBackend,SearchFilter)
    search_fields = [
        "names",
        "last_names",
        "document_type"
    ]
    filterset_class = PersonFilter
    ordering_fields = ["created_at"]
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted_at = datetime.datetime.now()
        count_documents = (
            Person.objects.filter(
                document__icontains=instance.document + '_deleted'
            ).values('document').count()
        )
        instance.document = instance.document + '_deleted' + str(count_documents + 1)
        instance.save()
        return Response(
            {"message": "Eliminado Correctamente"},
            status= status.HTTP_200_OK
        )
        

