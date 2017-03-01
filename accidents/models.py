"""
THIS APP IS USED TO HANDLE ACCIDENT RELATED INFO AND PROCESSES
"""
from django.db import models
from suvozac import settings
from core.models import (
    Vehicle,
    MalfunctionType,
    Region
)

user_model = settings.AUTH_USER_MODEL


class Malfunction(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    mf_type = models.ForeignKey(MalfunctionType, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
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
