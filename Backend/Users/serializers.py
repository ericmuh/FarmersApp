from .models import District,Subcounty, Officer
from rest_framework import serializers

class DistrictSerializer(serializers.ModelSerializer):
    model = District
    fields = '__all__'

class SubcountySerializer(serializers.ModelSerializer):
    model = Subcounty
    fields = '__all__'

class OfficerSerializer(serializers.ModelSerializer):
    model = Officer
    fields = '__all__'