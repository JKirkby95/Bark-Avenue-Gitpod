from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import AppointmentForm

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
            form.save()
            # Redirect to a success page or home page
            return redirect('index')
        return render(request, self.template_name, {'form': form})

class LoginView(TemplateView):
    template_name = 'login.html'
