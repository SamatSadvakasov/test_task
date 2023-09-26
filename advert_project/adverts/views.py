from rest_framework import generics
from .models import Advert
from .serializers import AdvertSerializer

class AdvertList(generics.ListCreateAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer

class AdvertDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer

    def perform_update(self, serializer):
        serializer.instance.views += 1
        serializer.instance.save()
