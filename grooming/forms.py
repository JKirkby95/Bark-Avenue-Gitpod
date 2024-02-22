from django import forms
from .models import Appointment, Groomer


class AppointmentForm(forms.ModelForm):
    customer = forms.CharField(max_length=100)
    pet = forms.CharField(max_length=100)

    class Meta:
        model = Appointment
        fields = [
            'appointment_date',
            'appointment_time',
            'customer',
            'pet',
            'groomer',
            'service',
            ]
        labels = {
            'appointment_date' : 'Select a date for your appointment.',
            'appointment_time' : 'Select a time for you appointment.',
            'groomer' : 'Select a groomer.',
            'pet' : 'What is your dogs name?',
            'customer' : 'What is your full name?',
        }
        widgets = {
            'appointment_date' : forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                }
            ),
            'appointment_time' : forms.TimeInput(
                attrs={
                    'type': 'time',
                    'class': 'form-control',
                }
            ),
        }
