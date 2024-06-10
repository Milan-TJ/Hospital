from django.urls import path
from .import views
from django.views.generic import RedirectView


urlpatterns = [
    path('',views.home,name="home"),
    path('AboutUs/',views.AboutUs,name="AboutUs"),
    path('Doctorlogin/',views.Doctorlogin,name="Doctorlogin"),
    path('Patientlogin/',views.Patientlogin,name="Patientlogin"),
    path('DoctorRegister/',views.DoctorRegister,name="DoctorRegister"),
    path('PatientRegister/',views.PatientRegister,name="PatientRegister"),
    path('EditDoctor/<str:pk>',views.EditDoctor,name="EditDoctor"),
    path('EditPatient/<str:pk>',views.EditPatient,name="EditPatient"),
    path('ViewDetails/<str:pk>',views.ViewDetails,name="ViewDetails"),
    path('ViewDetails/',views.ViewDetails,name="ViewDetails"),
    path('DoctorView/',views.DoctorView,name="DoctorView"),
    path('AdminView/',views.AdminView,name="AdminView"),
]

