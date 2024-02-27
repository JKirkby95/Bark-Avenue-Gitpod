from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Groomer(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.CharField(max_length=100)
    groomer = models.ForeignKey(Groomer, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return f"Appointment for {self.pet} on {self.appointment_date}"



# class' for the customer , pet ,groomer and appointments 
# class Customer(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     phone_number = models.CharField(max_length=20)
#     address = models.TextField()

#     def __str__(self):
#         return self.name

# class Pet(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     breed = models.CharField(max_length=100)
#     age = models.IntegerField()
#     comments = models.TextField(blank=True)

#     def __str__(self):
#         return self.name
