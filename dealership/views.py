from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from .models import Car, Contact,Appointment

def home(request):
    cars = Car.objects.all().order_by('priority')
    return render(request, 'pages/home.html', {'cars': cars})

def details(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'pages/details.html', {'car': car})

def search(request):
    query = request.GET.get('q')
    if query:
        cars = CarByCompany.objects.filter(
            Q(name__icontains=query) | Q(company__icontains=query)
        )
    else:
        cars = Car.objects.all()
    return render(request, 'pages/home.html', {'cars': cars, 'query': query})

def aboutus(request):
    return render(request, 'pages/aboutus.html')

def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact.objects.create(name=name, phone=phone, email=email, subject=subject, message=message)
        
        # Use the messages framework to add a success message
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contactus')
    
    return render(request, 'pages/contactus.html')

def services(request):
    return render(request,'pages/services.html')



from .models import CarByCompany

def cars_by_company(request, company_name):
    cars_by_company = CarByCompany.objects.filter(company=company_name).order_by('priority')
    return render(request, 'pages/cars_by_company.html', {'cars_by_company': cars_by_company, 'company_name': company_name})

def details_2(request, CarByCompany_id):
    car = get_object_or_404(CarByCompany, id=CarByCompany_id)
    return render(request, 'pages/details_2.html', {'car': car})


def filter_cars(request):
    # Retrieve query parameters from the GET request
    brand = request.GET.get('brand')
    year = request.GET.get('year')
    budget = request.GET.get('price')

    # Start with all cars
    cars = CarByCompany.objects.all()

    # Apply filters based on user input
    if brand:
        cars = cars.filter(company__iexact=brand)
    if year:
        cars = cars.filter(year=year)
    if budget:
        cars = cars.filter(price__lte=budget)

    # Pass the filtered cars to the template
    return render(request, 'pages/filter_cars.html', {'cars_by_company': cars})


def appointment(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        date = request.POST.get('date')
        time = request.POST.get('time')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Now include the date and time fields when creating the Appointment object
        Appointment.objects.create(
            name=name,
            phone=phone,
            email=email,
            date=date,
            time=time,
            subject=subject,
            message=message
        )
        
        # Use the messages framework to add a success message
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('appointment')

    return render(request, 'pages/appointment.html')

def terms_and_conditions(request):
    return render(request,'pages/Terms_and_Conditions.html')

def privacy_policy(request):
    return render(request,'pages/privacy_policy.html')

def complete_garage(request):
    cars_by_company = CarByCompany.objects.all()

    return render(request,'pages/complete_garage.html',{'cars_by_company':cars_by_company})

def detailing(request):
    return render(request,'pages/detailing.html')