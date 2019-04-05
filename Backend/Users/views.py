
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView
from .models import Officer, District, Subcounty, Parish, Farmer
from .serializers import OfficerSerializer, SubcountySerializer,ParishSerializer

class UserListView(ListCreateAPIView):
    queryset = Officer.objects.all()
    serializer_class = OfficerSerializer