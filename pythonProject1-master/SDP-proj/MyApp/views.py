from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from .models import Car, Order, Contact,Bike,Bus,OrderBike,OrderBus


def initial(request):
    return render(request, 'initial.html')


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html ')


def register(request):
    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['username']
        number = request.POST['number']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        tosend = 'Thank you for registering with us, Hope you have a great journey by booking our vehicles.Regards From Team Rent Us!'
        if User.objects.filter(username=username).first():
            messages.error(request, "Username already taken")
            return redirect('register')
        if User.objects.filter(email=email).first():
            messages.error(request, "Email already taken")
            return redirect('register')

        if password != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        myuser = User.objects.create_user(username=username, email=email, password=password)
        myuser.name = name
        myuser.save()
        send_mail(
            'Thank you for contacting Rental Business System from our Website named Rent Us!',
            tosend,
            'surajkumar.sk.pika.0807@gmail.com',
            [email],
            fail_silently=False,
        )
        messages.success(request, "Your account has been successfully created!")
        return redirect('signin')


    else:
        print("error")
        return render(request, 'register.html')


def signin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('signin')

    else:
        print("error")
        return render(request, 'login.html')


def signout(request):
    logout(request)
    return redirect('initial')


def vehicles(request):
    cars = Car.objects.all()
    params = {'car': cars}
    return render(request, 'vehicles.html ', params)

def vehicles1(request):
    bikes = Bike.objects.all()
    params = {'bike': bikes}
    return render(request, 'vehicles1.html ', params)

def vehicles2(request):
    buses = Bus.objects.all()
    params = {'bus': buses}
    return render(request, 'vehicles2.html ', params)


def bill(request):
    cars = Car.objects.all()
    params = {'cars': cars}
    return render(request, 'bill.html', params)

def bill1(request):
    bikes = Bike.objects.all()
    params = {'bikes': bikes}
    return render(request, 'bill1.html', params)

def bill2(request):
    buses = Bus.objects.all()
    params = {'buses': buses}
    return render(request, 'bill2.html', params)


from django.shortcuts import render, redirect
from .models import Order

def order(request):
    if request.method == "POST":
        billname = request.POST.get('billname', '')
        billemail = request.POST.get('billemail', '')
        billphone = request.POST.get('billphone', '')
        billaddress = request.POST.get('billaddress', '')
        billcity = request.POST.get('billcity', '')
        cars11 = request.POST['cars11']
        dayss = request.POST.get('dayss', '')
        date = request.POST.get('date', '')
        fl = request.POST.get('fl', '')
        tl = request.POST.get('tl', '')
        if 'aadhar' in request.FILES:
            aadhar_card = request.FILES['aadhar']
        else:
            aadhar_card = None

        if 'driving_license' in request.FILES:
            driving_license = request.FILES['driving_license']
        else:
            driving_license = None

        if 'passport_photo' in request.FILES:
            passport_photo = request.FILES['passport_photo']
        else:
            passport_photo = None

        order = Order(name=billname, email=billemail, phone=billphone, address=billaddress, city=billcity, cars=cars11,
                      days_for_rent=dayss, date=date, loc_from=fl, loc_to=tl,aadhar_card=aadhar_card, driving_license=driving_license, passport_photo=passport_photo)
        order.save()
        return redirect('home')
    else:
        print("error")
        return render(request, 'bill.html')


def order1(request):
    if request.method == "POST":
        billname = request.POST.get('billname', '')
        billemail = request.POST.get('billemail', '')
        billphone = request.POST.get('billphone', '')
        billaddress = request.POST.get('billaddress', '')
        billcity = request.POST.get('billcity', '')
        bikes11 = request.POST['bikes11']
        dayss = request.POST.get('dayss', '')
        date = request.POST.get('date', '')
        fl = request.POST.get('fl', '')
        tl = request.POST.get('tl', '')
        if 'aadhar' in request.FILES:
            aadhar_card = request.FILES['aadhar']
        else:
            aadhar_card = None

        if 'driving_license' in request.FILES:
            driving_license = request.FILES['driving_license']
        else:
            driving_license = None

        if 'passport_photo' in request.FILES:
            passport_photo = request.FILES['passport_photo']
        else:
            passport_photo = None

        order = OrderBike(name=billname, email=billemail, phone=billphone, address=billaddress, city=billcity, bike=bikes11,
                      days_for_rent=dayss, date=date, loc_from=fl, loc_to=tl,aadhar_card=aadhar_card, driving_license=driving_license, passport_photo=passport_photo)
        order.save()
        return redirect('home')
    else:
        print("error")
        return render(request, 'bill1.html')

def order2(request):
    if request.method == "POST":
        billname = request.POST.get('billname', '')
        billemail = request.POST.get('billemail', '')
        billphone = request.POST.get('billphone', '')
        billaddress = request.POST.get('billaddress', '')
        billcity = request.POST.get('billcity', '')
        buses11 = request.POST['buses11']
        dayss = request.POST.get('dayss', '')
        date = request.POST.get('date', '')
        fl = request.POST.get('fl', '')
        tl = request.POST.get('tl', '')
        if 'aadhar' in request.FILES:
            aadhar_card = request.FILES['aadhar']
        else:
            aadhar_card = None

        if 'driving_license' in request.FILES:
            driving_license = request.FILES['driving_license']
        else:
            driving_license = None

        if 'passport_photo' in request.FILES:
            passport_photo = request.FILES['passport_photo']
        else:
            passport_photo = None

        order = OrderBus(name=billname, email=billemail, phone=billphone, address=billaddress, city=billcity, bus=buses11,
                      days_for_rent=dayss, date=date, loc_from=fl, loc_to=tl,aadhar_card=aadhar_card, driving_license=driving_license, passport_photo=passport_photo)
        order.save()
        return redirect('home')
    else:
        print("error")
        return render(request, 'bill2.html')


def contact(request):
    if request.method == "POST":
        contactname = request.POST.get('contactname', '')
        contactemail = request.POST.get('contactemail', '')
        contactnumber = request.POST.get('contactnumber', '')
        contactmsg = request.POST.get('contactmsg', '')
        tosend = contactmsg + '.....................................................This is just an acknowledgement'
        contact = Contact(name=contactname, email=contactemail, phone_number=contactnumber, message=contactmsg)
        contact.save()
        send_mail(
            'Thank you for contacting Rental System',
            tosend,
            'surajkumar.sk.pika.0807@gmail.com',
            [contactemail],
            fail_silently=False,
        )
    return render(request, 'contact.html ')


