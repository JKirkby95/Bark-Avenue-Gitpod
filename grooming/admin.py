from django.contrib import admin
from .models import Customer , Pet , Groomer , Appointment

admin.site.register(Customer)
admin.site.register(Pet)
admin.site.register(Groomer)
admin.site.register(Appointment)

