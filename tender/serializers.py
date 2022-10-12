from rest_framework import serializers
from tender.models import Company, Project, Registrant, Item

class LazyRefSerializer(serializers.ModelSerializer):
    def __init__(self, ref, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self._reference_as_string = ref
        self._reference_as_serializer = None

    def __getattr__(self, item):
        return getattr(self._reference_as_serializer, item)

    def __getattribute__(self, attr):
        # When first trying to use its attributes, it imports and initializes the original serializer
        # The 'not in' check is to avoid infinite loops. _creation_counter is called when initializing the serializer which uses this LazyRefSerializer field
        if attr not in ['args', 'kwargs', '_reference_as_string', '_reference_as_serializer', '_creation_counter'] and self._reference_as_serializer is None:
            referenced_serializer = import_from_string(self._reference_as_string, '')
            self._reference_as_serializer = referenced_serializer(*self.args, **self.kwargs)
            self.__class__ = referenced_serializer
            self.__dict__.update(self._reference_as_serializer.__dict__)
        return object.__getattribute__(self, attr)

class CompanySerializer(serializers.ModelSerializer):
    registrations = LazyRefSerializer('serializers.RegistrantSerializer', many=True, read_only=True)
    class Meta:
        model = Company
        fields = ['id','user_id','company_name','pt_name','npwp','registrations','created_at','updated_at']

class ProjectSerializer(serializers.ModelSerializer):
    registrants = LazyRefSerializer('serializers.RegistrantSerializer', many=True, read_only=True)
    class Meta:
        model = Project
        fields = ['id','title','description','closed_at','chosen_registrat',]

class RegistrantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registrant
        fields = []

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = []