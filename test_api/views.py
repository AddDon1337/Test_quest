from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from test_api.models import Deal
from test_api.serializers import DealSerializer

# Create your views here.

@csrf_exempt
def deal_list(request):

       #List all code deals, or create a new deal.

    if request.method == 'GET':
        deals = Deal.objects.all()
        serializer = DealSerializer(deals, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DealSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def deal_detail(request, pk):
    """
    Retrieve, update or delete a code deal.
    """
    try:
        deal = Deal.objects.get(pk=pk)
    except Deal.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DealSerializer(deal)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DealSerializer(deal, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        deal.delete()
        return HttpResponse(status=204)
