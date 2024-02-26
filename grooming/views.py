from django.shortcuts import render, redirect
from django.views.generic import TemplateView , FormView
from .forms import AppointmentForm , SignUpForm , LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


class IndexView(TemplateView):
    template_name = 'index.html'

class BookingView(TemplateView):
    template_name = 'booking.html'

    def get(self, request):
        form = AppointmentForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            # Redirect to a success page or home page
            return redirect('index')
        return render(request, self.template_name, {'form': form})


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

