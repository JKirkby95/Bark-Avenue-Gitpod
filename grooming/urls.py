from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('booking/', views.BookingView.as_view(), name='booking'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('appointments/', views.AppointmentsView.as_view(), name='appointments'),
    path('pricing/', views.PriceView.as_view(), name='pricing'),
    path('edit-appointment/<int:appointment_id>/', views.EditAppointmentView.as_view(), name='edit_appointment'),
    path('delete-appointment/<int:appointment_id>/', views.DeleteAppointmentView.as_view(), name='delete_appointment'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
