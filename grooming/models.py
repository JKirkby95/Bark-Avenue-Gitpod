from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):
    '''
    class for the services provided
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Groomer(models.Model):
    '''
    class for the groomers available
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    '''
    class for the full appointment details
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.CharField(max_length=100)
    groomer = models.ForeignKey(Groomer, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return f"Appointment for {self.pet} on {self.appointment_date}"
