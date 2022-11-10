from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="index"),
    path('login',views.Login,name="login"),
    path('register',views.Register,name="register"),
    path('admin_welcome',views.AdminWelcome,name="admin_welcome"),
    path('doctor_welcome',views.DoctorWelcome,name="doctor_welcome"),
    path('patient_welcome',views.PatientWelcome,name="patient_welcome"),
    path('logout',views.Logout,name="logout"),
]