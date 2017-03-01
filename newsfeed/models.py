"""
THIS APP IS FOR HANDLING ROAD CONDITIONS INFO
"""
from django.db import models
from suvozac import settings
from core.models import Region

user_model = settings.AUTH_USER_MODEL


class RoadCondition(models.Model):
    region = models.ForeignKey(Region, null=True, on_delete=models.SET_NULL)
    driver = models.ForeignKey(user_model, null=True, on_delete=models.SET_NULL)
    rc_desc = models.TextField()
    """
        TODO: take care of photos here
        also watch out for automatic datetime
        geo_lat = models.DDecimalField(max_digits=8, decimal_places=3)
        geo_long = models.DecimalField(max_digits=8, decimal_places=3)
    """
    date_time = models.DateTimeField(auto_now_add=True)
    accuracy = models.FloatField(default=0)  # is the post about RC correct
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
