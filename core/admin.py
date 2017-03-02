from django.contrib import admin
from .models import (
    CustomUser, DriverProfile, ServiceProfile,
    MalfunctionType, ServiceMFType, ServiceRegion,
    ServiceVehicleType, Region, Vehicle, VehicleType)

admin.site.register(CustomUser)
admin.site.register(DriverProfile)
admin.site.register(ServiceProfile)
admin.site.register(Region)
admin.site.register(VehicleType)
admin.site.register(Vehicle)
admin.site.register(MalfunctionType)
admin.site.register(ServiceMFType)
admin.site.register(ServiceRegion)
admin.site.register(ServiceVehicleType)
