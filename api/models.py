from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from suvozac import settings

user_model = settings.AUTH_USER_MODEL


class CustomUser(AbstractUser):
    type_choices = (
        ('S', 'Service'),
        ('D', 'Driver'),
    )
    user_type = models.CharField(max_length=2, null=False, blank=False,
                                 choices=type_choices,
                                 default='D')


class ServiceProfile(models.Model):
    user = models.OneToOneField(user_model, on_delete=models.CASCADE)
    service_tel1 = models.CharField(max_length=20)
    service_tel2 = models.CharField(max_length=20)
    hours_start = models.TimeField(blank=False)
    hours_end = models.TimeField(blank=False)
    # Had to separate working hours by days to be precise on weekend
    sat_hours_start = models.TimeField(blank=True, null=True)
    sat_hours_end = models.TimeField(blank=True, null=True)
    sun_hours_start = models.TimeField(blank=True, null=True)
    sun_hours_end = models.TimeField(blank=True, null=True)
    geo_lat = models.DecimalField()
    geo_long = models.DecimalField()
    rate = models.DecimalField(default=0)
    """
        TODO: service images handling
        Also discuss about rate in this table and custom save() in SolvedMalfunction
        for it to update every time the user rates the service
    """


class DriverProfile(models.Model):
    user = models.OneToOneField(user_model, on_delete=models.CASCADE)
    driver_tel = models.CharField(max_length=20)
    """
        TODO: Driver images handling
    """


class VehicleType(models.Model):
    vehicle_type_choices = (
        ('C', 'Car'),
        ('T', 'Truck'),
    )

    type = models.CharField(max_length=2, null=False, blank=False,
                            choices=vehicle_type_choices,
                            default='C')
    """
        TODO: add all car makes to ensure equality between those, and types that services can handle
    """
    make = models.CharField(max_length=20)


class Vehicle(models.Model):
    type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    model = models.CharField(max_length=30)
    """
        TODO: add all models to ensure equality between those and car makes
        manage photos here also
    """
    ccm = models.IntegerField()
    """
        fuel types:
        0 - diesel
        1 - gasoline
        2 - LPG / liquid petroleum gas
        3 - metane
    """
    fuel_type = models.IntegerField()
    first_registration = models.IntegerField()


class ServiceVehicleType(models.Model):
    service = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)


class Region(models.Model):
    region_name = models.CharField(max_length=30)
    """
        TODO: think about setting region choices
        think about region coordinates!!!
    """
    geo_lat = models.DecimalField()
    geo_long = models.DecimalField()


class ServiceRegion(models.Model):
    service = models.ForeignKey(user_model, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)


class MalfunctionType(models.Model):
    mf_type = models.IntegerField(null=False, blank=False)  # 0 - engine, 1 - slepsluzba etc.
    """
        TODO:
        mf_type_choices = (
        ('')
        )
    """


class Malfunction(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    """
        TODO: think about changing the save() method instead of using auto_now_add
    """
    mf_desc = models.TextField(max_length=200)
    """
        TODO:
        think about adding those but maybe the region will be enough:
        geo_lat = models.DecimalField()
        geo_long = models.DecimalField()
    """
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    mf_type = models.ForeignKey(MalfunctionType, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)


class ServiceMFType(models.Model):
    service = models.ForeignKey(user_model, on_delete=models.CASCADE)
    mf_type = models.ForeignKey(MalfunctionType, on_delete=models.CASCADE)


class Application(models.Model):
    service = models.ForeignKey(user_model, on_delete=models.CASCADE)
    malfunction = models.ForeignKey(Malfunction, on_delete=models.CASCADE)
    """
        TODO: think about changing the save() method instead of using auto_now_add
    """
    date_time = models.DateTimeField(auto_now_add=True)


class SolvedMalfunction(models.Model):
    application = models.ForeignKey(Application, null=True, on_delete=models.SET_NULL)
    """
    Other, but redundant solution
    service = models.ForeignKey(user_model)
    malfunction = models.ForeignKey(Malfunction)
    """
    repair_rate = models.IntegerField()
    repair_desc = models.TextField(max_length=200)
    """
        TODO: think about custom save() in this one too
    """
    date_time = models.DateTimeField(auto_now_add=True)


"""
    ROAD CONDITIONS PART
"""


class RoadCondition(models.Model):
    rc_desc = models.TextField()
    """
        TODO: take care of photos here
        also watch out for automatic datetime
        geo_lat = models.DecimalField()
        geo_long = models.DecimalField()
    """
    date_time = models.DateTimeField(auto_now_add=True)
    accuracy = models.DecimalField(default=0)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL)
    driver = models.ForeignKey(user_model, on_delete=models.SET_NULL)
    """
        watch out for redundancy in accuracy!!!
        (maybe should be updated with adequate avg from comments table below)
    """


class RoadConditionComment(models.Model):
    user = models.ForeignKey(user_model, on_delete=models.CASCADE)
    road_condition = models.ForeignKey(RoadCondition, on_delete=models.CASCADE)
    true = models.IntegerField(default=1)
    additional_info = models.TextField(max_length=200)
    """
        auto_now_add story once again -.-
    """
    date_time = models.DateTimeField(auto_now_add=True)
