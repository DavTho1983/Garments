from rest_framework import generics

from Styling.models import Garments
from Styling.serializers import GarmentsSerializer

# Create your views here.
class GarmentsAPIListView(generics.ListAPIView):
    queryset = Garments.objects.all()
    serializer_class = GarmentsSerializer


class GarmentsAPIID(generics.RetrieveAPIView):
    queryset = Garments.objects.all()
    serializer_class = GarmentsSerializer
