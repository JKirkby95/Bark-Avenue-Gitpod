from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('booking/', views.BookingView.as_view(), name='booking'),
]