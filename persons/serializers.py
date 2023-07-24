from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        #fields = '__all__' # Para que devuelva todos los campos.
        exclude = ["deleted_at"] # Para excluir cierta cantidad de campos.