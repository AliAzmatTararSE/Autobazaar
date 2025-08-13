# admin.py
from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from .models import Car, CarImage, Bike,Contact,CarByCompany,CarByCompanyImage,Appointment,SoldCar


class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name','id', 'year', 'mileage', 'color', 'company', 'car_type', 'price','video','priority')  # Add new fields here
    search_fields = ('model', 'model_number', 'company')  # Optional: Add searchable fields
    inlines = [CarImageInline]
    
    

    ordering = ['priority']  # Orders the cars by priority in the admin panel

    # Override save_model to handle priority shift in the admin
    def save_model(self, request, obj, form, change):
     if change:  # Update
         old_priority = Car.objects.get(pk=obj.pk).priority
         if obj.priority != old_priority:
             if obj.priority > old_priority:
                 # Shift cars down between old_priority and new_priority
                 cars_to_shift = Car.objects.filter(priority__gt=old_priority, priority__lte=obj.priority).exclude(pk=obj.pk).order_by('priority')
                 for car in cars_to_shift:
                     car.priority -= 1
                     car.save()
             else:
                 # Shift cars up between new_priority and old_priority
                 cars_to_shift = Car.objects.filter(priority__gte=obj.priority, priority__lt=old_priority).exclude(pk=obj.pk).order_by('-priority')
                 for car in cars_to_shift:
                     car.priority += 1
                     car.save()
     else:  # New entry
         cars_to_shift = Car.objects.filter(priority__gte=obj.priority).order_by('-priority')
         for car in cars_to_shift:
             car.priority += 1
             car.save()
     obj.save()
     
     super().save_model(request, obj, form, change) 
   

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','id', 'email', 'formatted_subject', 'phone', 'submitted_at', 'formatted_message','checked_status')
    search_fields = ('name', 'email', 'subject')
    readonly_fields = ('submitted_at',)

    def formatted_subject(self, obj):
        return format_html(
            '<div style="white-space: normal; word-wrap: break-word; max-width: 300px;">{}</div>',
            obj.subject
        )
    formatted_subject.short_description = 'Subject'

    def formatted_message(self, obj):
        return format_html(
            '<div style="white-space: normal; word-wrap: break-word; max-width: 300px;">{}</div>',
            obj.message
        )
    formatted_message.short_description = 'Message'

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ('model', 'model_number')
    search_fields = ('model', 'model_number')



class CarByCompanyImageInline(admin.TabularInline):
    model= CarByCompanyImage
    extra = 1

@admin.register(CarByCompany)
class CarByCompanyAdmin(admin.ModelAdmin):
    list_display = ('name','id','year','mileage','color', 'company', 'car_type', 'price','video','formatted_description', 'priority')
    ordering = ['priority']
    inlines = [CarByCompanyImageInline]

    

    def formatted_description(self, obj):
        return format_html(
            '<div style="white-space: normal; word-wrap: break-word; max-width: 300px; overflow: hidden; text-overflow: ellipsis;">{}</div>',
            obj.description
        )
    formatted_description.short_description = 'Description'


    def save_model(self, request, obj, form, change):
        if not change:  # If adding a new car
            # Shift priorities of other cars from the same company
            CarByCompany.objects.filter(company=obj.company, priority__gte=obj.priority).update(priority=models.F('priority') )
        
        super().save_model(request, obj, form, change)



@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name','id', 'email','date','time', 'formatted_subject', 'phone', 'submitted_at', 'formatted_message','checked_status')
    search_fields = ('name', 'email', 'subject')
    readonly_fields = ('submitted_at',)

    def formatted_subject(self, obj):
        return format_html(
            '<div style="white-space: normal; word-wrap: break-word; max-width: 300px;">{}</div>',
            obj.subject
        )
    formatted_subject.short_description = 'Subject'

    def formatted_message(self, obj):
        return format_html(
            '<div style="white-space: normal; word-wrap: break-word; max-width: 300px;">{}</div>',
            obj.message
        )
    formatted_message.short_description = 'Message'


@admin.register(SoldCar)
class SoldCarAdmin(admin.ModelAdmin):
    list_display=('name','id','company','year','car_type','price','mileage','color','date','description','Profit')


