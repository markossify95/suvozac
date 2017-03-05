"""
THIS APP IS FOR CORE FUNCTIONALITY
IT IS USED FOR AUTH AND IT HANDLES ALL THE NECESSARY INFO ABOUT CLIENTS
"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from suvozac import settings

# FOR LATER ON :D
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.sessions import HUA
# from django.sessions import bakaaa

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
    geo_lat = models.DecimalField(max_digits=8, decimal_places=6)
    geo_long = models.DecimalField(max_digits=8, decimal_places=6)
    rate = models.FloatField(default=0)
    """
        TODO: service images handling
        Also discuss about rate in this table and custom save() in SolvedMalfunction
        for it to update every time the user rates the service
    """


"""
@receiver(post_save, sender=user_model)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ServiceProfile.objects.create(user=instance)


@receiver(post_save, sender=user_model)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
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
    """
    USER CAN'T BE NULL IN PRODUCTION, CHANGE IT ON DBMS CHANGE!!!!!! 'FALA, DULE.
    """
    user = models.ForeignKey(user_model, null=True, on_delete=models.CASCADE)
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
    service = models.ForeignKey(user_model, on_delete=models.CASCADE)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)


class Region(models.Model):
    region_name = models.CharField(max_length=30)
    """
        TODO: think about setting region choices
        think about region coordinates!!!
    """
    geo_lat = models.DecimalField(max_digits=8, decimal_places=6)
    geo_long = models.DecimalField(max_digits=8, decimal_places=6)


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


class ServiceMFType(models.Model):
    service = models.ForeignKey(user_model, on_delete=models.CASCADE)
    mf_type = models.ForeignKey(MalfunctionType, on_delete=models.CASCADE)
