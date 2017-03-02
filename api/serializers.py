from rest_framework import serializers
from core.models import *
from accidents.models import *
from newsfeed import *


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    #ToDo
    class Meta:
        model = Vehicle
        fields = '__all__'


class ServiceVehicleTypeSerializer(serializers.ModelSerializer):
    #ToDo
    class Meta:
        model = ServiceVehicleType
        fields = ()


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class ServiceRegionSerializer(serializers.ModelSerializer):
    #ToDo
    class Meta:
        model = ServiceRegion
        fields = '__all__'


class MalfunctionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MalfunctionType
        fields = '__all__'


class ServiceMFTypeSerializer(serializers.ModelSerializer):
    mf_type = MalfunctionTypeSerializer()
    #ToDo
    class Meta:
        model = ServiceMFType
        fields = '__all__'
