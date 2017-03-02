from rest_framework import serializers
from core.models import (CustomUser, DriverProfile, ServiceProfile)


#  These 3 will be used for adding new users
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


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
