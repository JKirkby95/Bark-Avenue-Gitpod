from django import forms
from .models import Appointment, Groomer
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import time

class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            ]

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        # Perform additional validation if needed
        if not username:
            raise forms.ValidationError("Username is required")
        if not password1:
            raise forms.ValidationError("Password is required")
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data

        
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        # Perform additional validation if needed
        if not username:
            raise forms.ValidationError("Username is required")
        if not password:
            raise forms.ValidationError("Password is required")

        return cleaned_data


class AppointmentForm(forms.ModelForm):
    pet = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    appointment_time = forms.ChoiceField(choices=[], widget=forms.Select(attrs={'class': 'form-control'}))


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Generate choices for appointment time slots from 9:00 to 17:00 in half-hour intervals
        time_slots = [('',  '---------')]
        current_time = time(9, 0)  # Start from 9:00 AM
        while current_time <= time(17, 0):  # Stop at 5:00 PM
            time_slots.append((current_time.strftime('%H:%M'), current_time.strftime('%I:%M %p')))
            current_time = (current_time.replace(minute=current_time.minute + 30) if current_time.minute == 0 else current_time.replace(hour=current_time.hour + 1, minute=0))
        self.fields['appointment_time'].choices = time_slots

    class Meta:
        model = Appointment
        fields = [
            'appointment_date',
            'appointment_time',
            'pet',
            'groomer',
            'service',
            ]
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
            'groomer': forms.Select(attrs={'class': 'form-control'}),
            'service': forms.Select(attrs={'class': 'form-control'}),
        }
