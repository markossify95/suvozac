from rest_framework import serializers
from core.models import (CustomUser, DriverProfile, ServiceProfile)
from django.contrib.auth import hashers


#  These 3 will be used for adding new users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    # JEDAN OD MOJIH TOP 5 NAJLEPSIH POTEZA U DJANGU DO SADA.
    def create(self, validated_data):
        validated_data['password'] = hashers.make_password(validated_data['password'])
        return CustomUser.objects.create(**validated_data)

    """
    TODO do the same for update method (for users who are changing their passwords). Dive into DRF documentation
    """


class DriverProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverProfile
        fields = '__all__'


class ServiceProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProfile
        fields = '__all__'


# These two (DriverSerializer & ServiceSerializer) will be used for fetching appropriate results
class DriverSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = DriverProfile
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ServiceProfile
        fields = '__all__'
