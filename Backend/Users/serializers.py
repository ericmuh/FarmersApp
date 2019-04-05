from .models import District, Subcounty, Parish, Officer
from rest_framework import serializers
from django.contrib.auth import authenticate


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'


class SubcountySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcounty
        fields = '__all__'


class ParishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parish
        fields = '__all__'


class OfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Officer
        fields = ['username', 'email', 'login_id', 'password', 'Telephone', 'parish', ]


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Officer
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Officer( name=validated_data['username'],login_id=validated_data['login_id'], password=validated_data['password'], Telephone=validated_data['Telephone'], parish=validated_data['parish'])
        return user


class LoginSerializer(serializers.Serializer):
    login_id = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
