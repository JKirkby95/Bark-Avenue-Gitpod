from django.db import models

# class' for the customer , pet ,groomer and appointments 
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name

class Pet(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Groomer(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name

class Appointment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    groomer = models.ForeignKey(Groomer, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    # list of services to select from
    SERVICES_CHOICES = (
        ('Wash', 'Wash'),
        ('Wash and Cut', 'Wash and Cut'),
        ('Nails Cut', 'Nails Cut'),
        ('The Works', 'The Works'),
    )
    services = models.CharField(max_length=100, choices=SERVICES_CHOICES, default='Wash and Cut')
    # string returned with appointment information
    def __str__(self):
        return f"Appointment for {self.pet.name} on {self.appointment_date}"

