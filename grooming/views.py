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

class BookingView(TemplateView):
    template_name = 'booking.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        form = AppointmentForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            # Redirect to a success page or home page
            return redirect('index')
        return render(request, self.template_name, {'form': form})

class EditAppointmentView(TemplateView):
    template_name = 'edit_appointment.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, appointment_id):
        appointment = get_object_or_404(Appointment, id=appointment_id)
        form = AppointmentForm(instance=appointment)
        return render(request, self.template_name, {'form': form, 'appointment_id': appointment_id})

    def post(self, request, appointment_id):
        appointment = get_object_or_404(Appointment, id=appointment_id)
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            # Form is not valid, render the form again with errors
            return HttpResponseBadRequest("Form submission failed. Please check the form and try again.")


class DeleteAppointmentView(View):
    def post(self, request, appointment_id):
        appointment = get_object_or_404(Appointment, id=appointment_id)
        appointment.delete()
        return redirect('appointments')


class SignupView(FormView):
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = '/login/'  # Redirect to login page after successful signup

    def form_valid(self, form):
        form.save()  # Save the user instance
        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'  # Redirect to home page after successful login

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)  # Authenticate with username
        if user is not None:
            login(self.request, user)
            return redirect(self.get_success_url())
        else:
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
        # Retrieve the current user's appointments
        user_appointments = Appointment.objects.filter(user=self.request.user)
        context['user_appointments'] = user_appointments
        return context
    

class CustomLogoutView(LogoutView):
    def get_next_page(self):
        # Override the default behavior to redirect to the home screen
        return reverse_lazy('index')
