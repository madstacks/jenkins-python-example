from rest_framework import viewsets

from example.exampleapp.models import Person
from example.exampleapp.serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    class Meta:
        queryset = Person.objects.all()
        serializer_class = PersonSerializer
