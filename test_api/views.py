from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from test_api.models import Deal
from test_api.serializers import DealSerializer


# Create your views here.


@api_view(['GET', 'POST'])
def deal_list(request, format=None):
    """
    List all code deals, or create a new deal.
    """
    if request.method == 'GET':
        deal = Deal.objects.all()
        serializer = DealSerializer(deal, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def deal_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code deal.
    """
    try:
        deal = Deal.objects.get(pk=pk)
    except Deal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DealSerializer(deal)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DealSerializer(deal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        deal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
