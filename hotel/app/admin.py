from django.contrib import admin
from .models import Customer,Booking,Staff,Services
# Register your models here.

admin.site.register(Customer)
admin.site.register(Booking)
admin.site.register(Staff)
admin.site.register(Services)
