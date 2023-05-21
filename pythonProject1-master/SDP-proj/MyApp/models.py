from django.db import models


class Ownerl(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

class Ownerr(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    car_id = models.IntegerField(default=0)
    car_name = models.CharField(max_length=30, default="")
    car_desc = models.CharField(max_length=300, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="car/images", default="")

    def __str__(self):
        return self.car_name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=90, default="")
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=20, default="")
    address = models.CharField(max_length=500, default="")
    city = models.CharField(max_length=50, default="")
    cars = models.CharField(max_length=50, default="")
    days_for_rent = models.IntegerField(default=0)
    date = models.CharField(max_length=50, default="")
    loc_from = models.CharField(max_length=50, default="")
    loc_to = models.CharField(max_length=50, default="")
    aadhar_card = models.FileField(upload_to='documents/', blank=True, null=True)
    driving_license = models.FileField(upload_to='documents/', blank=True, null=True)
    passport_photo = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return self.name



class Contact(models.Model):
    message = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, default="")
    email = models.CharField(max_length=150, default="")
    phone_number = models.CharField(max_length=15, default="")
    message = models.TextField(max_length=500, default="")
    def __str__(self):
        return self.name

class ContactUs(models.Model):
    message = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, default="")
    email = models.CharField(max_length=150, default="")
    phone_number = models.CharField(max_length=15, default="")
    message = models.TextField(max_length=500, default="")
    def __str__(self):
        return self.name


class Bike(models.Model):
    bike_id = models.IntegerField(default=0)
    bike_name = models.CharField(max_length=30, default="")
    bike_desc = models.CharField(max_length=300, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="car/images", default="")

    def __str__(self):
        return self.bike_name


class OrderBike(models.Model):
    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=90, default="")
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=20, default="")
    address = models.CharField(max_length=500, default="")
    city = models.CharField(max_length=50, default="")
    bike = models.CharField(max_length=50, default="")
    days_for_rent = models.IntegerField(default=0)
    date = models.CharField(max_length=50, default="")
    loc_from = models.CharField(max_length=50, default="")
    loc_to = models.CharField(max_length=50, default="")
    aadhar_card = models.FileField(upload_to='documents/', blank=True, null=True)
    driving_license = models.FileField(upload_to='documents/', blank=True, null=True)
    passport_photo = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return self.name

class Bus(models.Model):
    bus_id = models.IntegerField(default=0)
    bus_name = models.CharField(max_length=30, default="")
    bus_desc = models.CharField(max_length=300, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="car/images", default="")

    def __str__(self):
        return self.bus_name

class OrderBus(models.Model):
    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=90, default="")
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=20, default="")
    address = models.CharField(max_length=500, default="")
    city = models.CharField(max_length=50, default="")
    bus = models.CharField(max_length=50, default="")
    days_for_rent = models.IntegerField(default=0)
    date = models.CharField(max_length=50, default="")
    loc_from = models.CharField(max_length=50, default="")
    loc_to = models.CharField(max_length=50, default="")
    aadhar_card = models.FileField(upload_to='documents/', blank=True, null=True)
    driving_license = models.FileField(upload_to='documents/', blank=True, null=True)
    passport_photo = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return self.name

class VehicleShop(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    business_na = models.CharField(max_length=100)
    business_address = models.CharField(max_length=200)
    business_ph = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Payment(models.Model):
    cardno = models.CharField(max_length=16)
    month = models.CharField(max_length=7)
    number = models.CharField(max_length=10)
    cvc = models.CharField(max_length=4)
    name = models.CharField(max_length=255)
    bill = models.DecimalField(max_digits=10, decimal_places=2)

class OwnerDocuments(models.Model):
    aadhar_card = models.FileField(upload_to='ownerdocs/')
    pan_card = models.FileField(upload_to='ownerdocs/')
    business_license = models.FileField(upload_to='ownerdocs/')
    vehicle_proof_documents = models.FileField(upload_to='ownerdocs/')
    vehicle_insurance_documents = models.FileField(upload_to='ownerdocs/')

class BankDetails(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20)
    ifsc_code = models.CharField(max_length=20)





