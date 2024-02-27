from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('booking/', views.BookingView.as_view(), name='booking'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('appointments/', views.AppointmentsView.as_view(), name='appointments'),
]