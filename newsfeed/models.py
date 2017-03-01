"""
THIS APP IS FOR HANDLING ROAD CONDITIONS INFO
"""
from django.db import models
from suvozac import settings
from core.models import Region

user_model = settings.AUTH_USER_MODEL


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
