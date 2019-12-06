from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from registration.models import users_socio
from registration.api.serializers import registration_serializer

"""class api_registration_view(viewsets.ModelViewSet):
    def list(self,request):
        queryset = users_socio.objects.all()
        serializer_class = registration_serializer
   return Response(serializer_class.data)
"""

@csrf_exempt
def registration_list(request,format=None):
    """
    List all code registration, or create a new registration.
    """
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