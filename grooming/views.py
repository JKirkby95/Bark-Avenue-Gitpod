from django.shortcuts import render, redirect , get_object_or_404
from django.views.generic import TemplateView, FormView, View
from .forms import AppointmentForm, SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Appointment
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.utils.decorators import method_decorator
from django.http import HttpResponseNotAllowed


class IndexView(TemplateView):
    ''' 
    Class for Home page view
    '''
    template_name = 'index.html'

class PriceView(TemplateView):
    ''' 
    Class for prices page view
    '''
    template_name = 'pricing.html'

class BookingView(TemplateView):
    ''' 
    Class for appointment booking page view
    '''
    template_name = 'booking.html'
    # login required for this page
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    # render the booking form from forms.py 
    def get(self, request):
        form = AppointmentForm()
        return render(request, self.template_name, {'form': form})
    # redirecting the user after the form is completed
    def post(self, request):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            # Redirect to a success page or home page
            return redirect('appointments')
        return render(request, self.template_name, {'form': form})

class EditAppointmentView(TemplateView):
    '''
    class for editing the appointments
    '''
    template_name = 'edit_appointment.html'
    # login required for this page
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    # getting the appointment id
    def get(self, request, appointment_id):
        appointment = get_object_or_404(Appointment, id=appointment_id)
        form = AppointmentForm(instance=appointment)
        return render(request, self.template_name, {'form': form, 'appointment_id': appointment_id})
    # saving the new appointment details and redirecting user
    def post(self, request, appointment_id):
        appointment = get_object_or_404(Appointment, id=appointment_id)
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointments')
        else:
            # Form is not valid, render the form again with errors
            return HttpResponseBadRequest("Form submission failed. Please check the form and try again.")


class DeleteAppointmentView(View):
    '''
    getting the appointment id to delete
    '''
    def post(self, request, appointment_id):
        appointment = get_object_or_404(Appointment, id=appointment_id)
        appointment.delete()
        return redirect('appointments')

    
class SignupView(FormView):
    '''
    class for the sign up page
    '''
    template_name = 'signup.html'
    # render the sign up form from forms.py
    form_class = SignUpForm
    # Redirect user to login page after successful signup
    success_url = '/login/'

    def form_valid(self, form):
        # Save the user for login
        form.save()  
        return super().form_valid(form)


class LoginView(FormView):
    ''' 
    class for login page view
    '''
    template_name = 'login.html'
    # render login form from forms.py
    form_class = LoginForm
    # Redirect user to home page after successful login
    success_url = '/'

    def form_valid(self, form):
          # Authenticating the login details
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect(self.get_success_url())
        else:
            # error message for incorrect login details
            messages.error(self.request, 'Invalid username or password')
            return super().form_invalid(form)

@method_decorator(login_required, name='dispatch')
class AppointmentsView(TemplateView):
    ''' 
    Class for viewing editing and deleting users appointments
    '''
    template_name = 'appointments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve the current users appointments
        user_appointments = Appointment.objects.filter(user=self.request.user)
        context['user_appointments'] = user_appointments
        return context

    
class CustomLogoutView(LogoutView):
    '''
    Class for handling log out function
    '''
    def get_next_page(self):
        # Return user to home screen when logged out
        return reverse_lazy('index')
