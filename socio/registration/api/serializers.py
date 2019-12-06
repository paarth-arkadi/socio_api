from rest_framework import serializers

from registration.models import users_socio
# from registration.models import socio_users
# from django.auth.models import User
class registration_serializer(serializers.ModelSerializer):
    # Api testing serializer
    class Meta:
        model = users_socio
        fields = '__all__'

"""
class registration_page1_serializer(serializers.ModelSerializer):
    class Meta:
        model = socio_users
        fields = '__all__'

"""

""" 
class registration_page1_user_auth_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password','first_name','last_name']
"""