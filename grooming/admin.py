from django.contrib import admin
from .models import Groomer, Appointment, Service

admin.site.register(Groomer)
admin.site.register(Appointment)
admin.site.register(Service)
