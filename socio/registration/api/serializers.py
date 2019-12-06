from rest_framework import serializers
from registration.models import users_socio

class registration_serializer(serializers.ModelSerializer):
    class Meta:
        model = users_socio
        fields = '__all__'
