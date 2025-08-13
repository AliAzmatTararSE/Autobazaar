from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('details/<int:car_id>/', views.details, name='details'),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('search/', views.search, name='search'),
    path('contactus/',views.contactus,name="contactus"),
    path('services/',views.services,name="services"),
    path('cars/company/<str:company_name>/', views.cars_by_company, name='cars_by_company'),
    path('details_2/<int:CarByCompany_id>/', views.details_2, name='details_2'),
    path('filter_cars/', views.filter_cars, name='filter_cars'),  # Add this line,
    path('appointment/',views.appointment,name="appointment"),
    path('termsandconditions/',views.terms_and_conditions,name="terms_and_conditions"),
    path('privacypolicy/',views.privacy_policy,name="privacy_policy"),
    path('completegarage/',views.complete_garage,name="complete_garage"),
    path('detailing/',views.detailing,name="detailing")
]
