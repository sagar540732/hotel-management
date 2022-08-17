from django.db import models
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True, )
    contact_number = models.PositiveIntegerField()
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_customer = models.BooleanField(default=False)
    is_service = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'




class Customer(models.Model):

    DOB = models.DateField()
    card_no = models.IntegerField()
    valid_id = models.ImageField(upload_to="images\customer")
    comment = models.TextField()

    def __str__(self):
        return self.firstname


class Booking(models.Model):
    ROOM_CHOICE = (
        ("1", "Deluxe"),
        ("2", "Suit"),
        ("3", "Honeymoon")
    )
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    DOB = models.DateTimeField()
    card_no = models.IntegerField()
    room_no = models.IntegerField()
    room_category = models.CharField(choices=ROOM_CHOICE, max_length=20)
    comment = models.TextField(max_length=200)
    upload_id = models.ImageField(upload_to="images\Booking")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="bookings")

    def __str__(self):
        return self.room_category


class Staff(models.Model):
    DEPARTMENT_NAME = (
        (1, "HR"),
        (2, "Chef/waiter"),
        (3, "Room services"),
        (4, "House-keeping"),
        (5, "security-staff"),
        (6, "other-staff")
    )
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    department_id = models.IntegerField()
    department_name = models.CharField(choices=DEPARTMENT_NAME, max_length=50)
    address = models.CharField(max_length=50)
    start_Date = models.DateField()
    end_Date = models.DateField()

    def __str__(self):
        return self.department_name


class Services(models.Model):
    SERVICES_NAME = (
        ("Resturant", "Resturant"),
        ("Catering", "Catering"),
        ("Cab/Bus", "Cab/Bus"),
        ("Laundary", "Laundary"),
        ("Invetatory", "Invetatory"),
        ("maintenance", (
            ("ele", "electrical"),
            ("plum", "Plumbing"),
            ("fur", "Furniture"),
            ("wast", "waste"),
        )
         ))
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    stat_Date = models.DateTimeField()
    end_Date = models.DateTimeField()
    working_hours = models.DateTimeField()
    comment = models.TextField(max_length=200)
    upload_id = models.ImageField(upload_to="images\Services")
    service_id = models.IntegerField()
    service_name = models.CharField(choices=SERVICES_NAME, max_length=50)

    def __str__(self):
        return self.service_name
