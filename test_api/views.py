
from test_api.models import Deal
from test_api.serializers import DealSerializer
from rest_framework import generics


# Create your views here.


class DealList(generics.ListCreateAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer


class DealDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
