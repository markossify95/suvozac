from django.contrib import admin
from .models import (
    Malfunction, Application, SolvedMalfunction
)

admin.site.register(Malfunction)
admin.site.register(Application)
admin.site.register(SolvedMalfunction)
