from django.db import models

class Car(models.Model):
    COMPANY_CHOICES=[
        ('Honda','Honda'),
        ('Toyota','Toyota'),
        ('Suzuki','Suzuki'),
        ('Nissan','Nissan'),
        ('Mercedes','Mercedes'),
        ('BMW','BMW'),
        ('Audi','Audi'),
        ('KIA','KIA'),
        ('Huyandai','Huyandai'),
        ('Changan','Changan'),
        ('Haval','Haval'),
        ('MG','MG')
    ]

    CAR_TYPE=[
        ('SUV','SUV'),
        ('Sedan','Sedan'),
        ('Hatchback','Hatchback'),
        ('Fourdoor','Fourdoor')
    ]
    
    YEAR_CHOICES=[
        ('2024','2024'),
('2023','2023'),
('2022','2022'),
('2021','2021'),
('2020','2020'),
('2019','2019'),
('2018','2018'),
('2017','2017'),
('2016','2016'),
('2015','2015'),
('2014','2014'),
('2013','2013'),
('2012','2012'),
('2011','2011'),
('2010','2010'),
('2009','2009'),
('2008','2008'),
('2007','2007'),
('2006','2006'),
('2005','2005'),
('2004','2004'),
('2003','2003'),
('2002','2002'),
('2001','2001'),
('2000','2000'),
('1999','1999'),
('1998','1998'),
('1997','1997'),
('1996','1996'),
('1995','1995'),
('1994','1994'),
('1993','1993'),
('1992','1992'),
('1991','1991'),
('1990','1990')
    ]
    name= models.CharField(max_length=100,null=True,blank=True)
    year = models.CharField(max_length=50,choices=YEAR_CHOICES, null=True, blank=True)
    mileage = models.IntegerField( null=True, blank=True)
    color = models.CharField(max_length=30, null=True, blank=True)
    company = models.CharField(max_length=100,choices=COMPANY_CHOICES, null=True, blank=True)
    car_type = models.CharField(max_length=50,choices=CAR_TYPE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField( null=True, blank=True)
    image = models.ImageField(upload_to='cars/', null=True, blank=True)
    video = models.FileField(upload_to='cars/videos/', null=True, blank=True)
    priority = models.IntegerField(default=0)
    

    
    
    def save(self, *args, **kwargs):
        if self.pk is None:  # New car is being added
            cars_to_shift = Car.objects.filter(priority__gte=self.priority).order_by('-priority')
        else:  # Updating an existing car
            old_priority = Car.objects.get(pk=self.pk).priority
            if self.priority != old_priority:
                if self.priority > old_priority:
                    # Shift cars down between old_priority and new_priority
                    cars_to_shift = Car.objects.filter(priority__gt=old_priority, priority__lte=self.priority).exclude(pk=self.pk).order_by('priority')
                    for car in cars_to_shift:
                        car.priority -= 1
                        car.save()
                else:
                    # Shift cars up between new_priority and old_priority
                    cars_to_shift = Car.objects.filter(priority__gte=self.priority, priority__lt=old_priority).exclude(pk=self.pk).order_by('-priority')
                    for car in cars_to_shift:
                        car.priority += 1
                        car.save()

        super(Car, self).save(*args, **kwargs)
  
    def delete(self, *args, **kwargs):
        car_priority = self.priority
        super(Car, self).delete(*args, **kwargs)
        cars_to_shift = Car.objects.filter(priority__gt=car_priority).order_by('priority')
        for car in cars_to_shift:
            car.priority -= 1
            car.save()

    def __str__(self):
        return self.name
    


class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='cars/')

    def __str__(self):
        return f"{self.car.name} Image"
    
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    phone = models.CharField(max_length=15, blank=True)  # Add phone field here
    submitted_at = models.DateTimeField(auto_now_add=True)
    checked_status=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"

class Bike(models.Model):
    model = models.CharField(max_length=50)
    model_number = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.model


class CarByCompany(models.Model):
    
    COMPANY_CHOICES=[
        ('Honda','Honda'),
        ('Toyota','Toyota'),
        ('Suzuki','Suzuki'),
        ('Nissan','Nissan'),
        ('Mercedes','Mercedes'),
        ('Bmw','Bmw'),
        ('Audi','Audi'),
        ('Kia','Kia'),
        ('Huyandai','Huyandai'),
        ('Changan','Changan'),
        ('Haval','Haval'),
        ('Mg','Mg')
    ]
    CAR_TYPE=[
        ('suv','Suv'),
        ('sedan','Sedan'),
        ('hatchback','Hatchback'),
        ('fourdoor','Fourdoor')
    ]
    
    YEAR_CHOICES=[
        ('2024','2024'),
('2023','2023'),
('2022','2022'),
('2021','2021'),
('2020','2020'),
('2019','2019'),
('2018','2018'),
('2017','2017'),
('2016','2016'),
('2015','2015'),
('2014','2014'),
('2013','2013'),
('2012','2012'),
('2011','2011'),
('2010','2010'),
('2009','2009'),
('2008','2008'),
('2007','2007'),
('2006','2006'),
('2005','2005'),
('2004','2004'),
('2003','2003'),
('2002','2002'),
('2001','2001'),
('2000','2000'),
('1999','1999'),
('1998','1998'),
('1997','1997'),
('1996','1996'),
('1995','1995'),
('1994','1994'),
('1993','1993'),
('1992','1992'),
('1991','1991'),
('1990','1990')
    ]
    name = models.CharField(max_length=100,null=True,blank=True)
    year = models.CharField(max_length=10,choices=YEAR_CHOICES,null=True,blank=True)
    mileage = models.IntegerField(  null=True, blank=True)
    color = models.CharField(max_length=30, null=True, blank=True)
    company = models.CharField(max_length=100,choices=COMPANY_CHOICES,null=True,blank=True)
    car_type=models.CharField(max_length=10,choices=CAR_TYPE,null=True,blank=True)
    description = models.TextField()
    price = models.IntegerField(null=True,blank=True)
    image = models.ImageField(upload_to='cars_by_company/')
    video = models.FileField(upload_to='cars_by_company/videos/', null=True, blank=True)
    priority = models.IntegerField(default=0)

    

    def save(self, *args, **kwargs):
        if self.pk:  # If this is an existing car (with a primary key)
            old_car = CarByCompany.objects.get(pk=self.pk)
            if old_car.priority != self.priority:  # If priority has changed
                if self.priority < old_car.priority:
                    # Shift priorities down between the new and old priority
                    CarByCompany.objects.filter(
                        company=self.company,
                        priority__gte=self.priority,
                        priority__lt=old_car.priority
                    ).update(priority=models.F('priority') + 1)
                else:
                    # Shift priorities up between the old and new priority
                    CarByCompany.objects.filter(
                        company=self.company,
                        priority__gt=old_car.priority,
                        priority__lte=self.priority
                    ).update(priority=models.F('priority') - 1)
        else:
            # Shift priorities of other cars if this is a new car (no primary key yet)
            CarByCompany.objects.filter(company=self.company, priority__gte=self.priority).update(priority=models.F('priority') + 1)
        
        super(CarByCompany, self).save(*args, **kwargs)

    
    
    def delete(self, *args, **kwargs):
        # Shift priorities of cars with higher priorities down
        CarByCompany.objects.filter(
            company=self.company,
            priority__gt=self.priority
        ).update(priority=models.F('priority') - 1)
        
        super(CarByCompany, self).delete(*args, **kwargs)
    
         
    def __str__(self):
        return f" {self.name}"


class CarByCompanyImage(models.Model):
    car_by_company = models.ForeignKey(CarByCompany, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='cars_by_company/')

    def __str__(self):
        return f"{self.car_by_company.company} {self.car_by_company.name} Image"


class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date=models.DateField(null=True)
    time=models.TimeField(null=True)
    subject = models.CharField(max_length=200)
    message= models.TextField()
    phone = models.CharField(max_length=15, blank=True)  # Add phone field here
    submitted_at = models.DateTimeField(auto_now_add=True)
    checked_status=models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
    


class SoldCar(models.Model):


    COMPANY_CHOICES=[
        ('Honda','Honda'),
        ('Toyota','Toyota'),
        ('Suzuki','Suzuki'),
        ('Nissan','Nissan'),
        ('Mercedes','Mercedes'),
        ('BMW','BMW'),
        ('Audi','Audi'),
        ('KIA','KIA'),
        ('Huyandai','Huyandai'),
        ('Changan','Changan'),
        ('Haval','Haval'),
        ('MG','MG')
    ]
    
    CAR_TYPE=[
        ('SUV','SUV'),
        ('Sedan','Sedan'),
        ('Hatchback','Hatchback'),
        ('Fourdoor','Fourdoor')
    ]
    
    YEAR_CHOICES=[
        ('2024','2024'),
('2023','2023'),
('2022','2022'),
('2021','2021'),
('2020','2020'),
('2019','2019'),
('2018','2018'),
('2017','2017'),
('2016','2016'),
('2015','2015'),
('2014','2014'),
('2013','2013'),
('2012','2012'),
('2011','2011'),
('2010','2010'),
('2009','2009'),
('2008','2008'),
('2007','2007'),
('2006','2006'),
('2005','2005'),
('2004','2004'),
('2003','2003'),
('2002','2002'),
('2001','2001'),
('2000','2000'),
('1999','1999'),
('1998','1998'),
('1997','1997'),
('1996','1996'),
('1995','1995'),
('1994','1994'),
('1993','1993'),
('1992','1992'),
('1991','1991'),
('1990','1990')
    ]

    company = models.CharField(max_length=100,choices=COMPANY_CHOICES,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    year = models.CharField(max_length=10,choices=YEAR_CHOICES,null=True,blank=True)
    car_type=models.CharField(max_length=10,choices=CAR_TYPE,null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    mileage = models.IntegerField(  null=True, blank=True)
    color = models.CharField(max_length=30, null=True, blank=True)
    date=models.DateField(null=True)
    Profit=models.CharField(max_length=8,null=True)
    
   
    

    description = models.TextField(default=0)

