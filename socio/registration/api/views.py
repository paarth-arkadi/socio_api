from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from registration.models import users_socio
# from django.auth.models import User

from registration.api.serializers import registration_serializer
#from registration.api.serializer import registration_page1_serializer
#from registration.api.serializer import registration_page1_user_auth_serializer

import json # For json to list conversion

@csrf_exempt
def registration_list(request,format=None):
    """
    List all code registration, or create a new registration.
    """
    # This is for testing
    if request.method == 'GET':
        queryset = users_socio.objects.all()
        serializer = registration_serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = registration_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def registration_detail(request, pk,format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    # This is for testing
    try:
        queryset = users_socio.objects.get(pk=pk)
    except queryset.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = registration_serializer(queryset)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = registration_serializer(queryset, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        queryset.delete()
        return HttpResponse(status=204)

"""
@csrf_exempt
def registration_page1_list(request,format=None):
    # This is for registration page1 
    if request.method == 'GET':
        queryset = socio_users.objects.all()
        serializer = registration_page1_serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = registration_page1_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
"""

"""
@csrf_exempt
def registration_page1_list(request,format=None):
    # This is for registration page1 
    if request.method == 'GET':
        queryset = socio_users.objects.all()
        serializer = registration_page1_serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = registration_page1_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
"""

"""
@csrf_exempt
def registration_page1_auth_user_list(request,format=None):
    # This is for registration page1 
    if request.method == 'GET':
        queryset = User.objects.all()
        serializer = registration_page1_auth_user_serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        mydata = json.loads(data)
        password = mydata['password']
        email = mydata['email']
        first_name = mydata['first_name']
        last_name = mydata['last_name']

        # Same password check added in the app layer
        if User.objects.filter(email=email).exists():
            messages.info(
            return JsonResponse(serializer.errors, status=400)
        
        user_auth = User.objects.create_user(username=email,email=email,password=password,first_name=first_name,last_name=last_name)
        user_auth.save()
        return JsonResponse(serializer.data, status=201)
        
"""