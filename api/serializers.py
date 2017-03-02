from rest_framework import serializers
from core.models import *
from accidents.models import *
from newsfeed.models import *
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


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    user = DriverSerializer()
    type = VehicleTypeSerializer()

    class Meta:
        model = Vehicle
        fields = ('user', 'type', 'model', 'ccm', 'fuel_type', 'first_registration')


"""
ToDo srediti ovo da vraca malo bolje podatke
"""


class ServiceVechileSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()
    vehicle_tupe = VehicleTypeSerializer()

    class Meta:
        model = ServiceVehicleType
        fields = ('service', 'vechile_type')


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


"""
ToDo ista spika kao ovo gore
"""


class ServiceRegionSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()
    region = RegionSerializer()

    class Meta:
        model = ServiceRegion
        fields = ('service', 'region')


class MalfunctionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MalfunctionType
        fields = '__all__'


class ServiceMFTypeSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()
    mf_type = ServiceMFType()

    class Meta:
        model = ServiceMFType
        fields = ('service', 'mf_type')


"""
Accidents serializers
"""


class MalfunctionSerializer(serializers.ModelSerializer):
    pass
