from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import Car, Contact, Bike, Bus, OrderBike, OrderBus ,Order,VehicleShop,ContactUs,Ownerl,Ownerr,Payment,OwnerDocuments,BankDetails


def payment(request):
    if request.method == 'POST':
        cardno = request.POST.get('cardno')
        month = request.POST.get('month')
        number = request.POST.get('number')
        cvc = request.POST.get('cvc')
        name = request.POST.get('name')
        bill = request.POST.get('bill')

        Payment.objects.create(
            cardno=cardno,
            month=month,
            number=number,
            cvc=cvc,
            name=name,
            bill=bill
        )

        return redirect('home')

    return render(request, 'payment.html')

def initial(request):
    return render(request, 'initial.html')

def adminhome(request):
    return render(request, 'adminhome.html')
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})



def settings(request):
    return render(request, 'settings.html')

def settings1(request):
    return render(request, 'settings1.html')

def help(request):
    return render(request, 'help.html')

def help1(request):
    return render(request, 'help1.html')

def help2(request):
    return render(request, 'help2.html')

def index(request):
   return render(request, 'index.html')

def index1(request):
   return render(request, 'index1.html')

def faqs(request):
    return render(request, 'faqs.html')

def faqs1(request):
    return render(request, 'faqs1.html')
def about(request):
    return render(request, 'about.html ')

def about1(request):
    return render(request, 'about1.html ')

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
        myuser.number = number
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

def registerowner(request):
    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['username']
        number = request.POST['number']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        tosend = 'Thank you for registering with us, Hope you have a great journey by booking our vehicles.Regards From Team Rent Us!'

        if password != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register-owner')

        if Ownerl.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('register-owner')
        if Ownerr.objects.filter(email=email).exists():
            messages.error(request, "Email already taken")
            return redirect('register-owner')

        owner = Ownerl(username=username, password=password)
        owner.save()

        owner = Ownerr(username=username, email=email, password=password, name=name, number=number)
        owner.name = name
        owner.number = number
        owner.save()

        send_mail(
            'Thank you for contacting Rental Business System from our Website named Rent Us!',
            tosend,
            'surajkumar.sk.pika.0807@gmail.com',
            [email],
            fail_silently=False,
        )
        messages.success(request, "Your account has been successfully created!")
        return redirect('signin-owner')
    else:
        return render(request, 'registerowner.html')
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

def signinowner(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        try:
            owner = Ownerl.objects.get(username=loginusername, password=loginpassword)
            return redirect('home-owner')
        except Ownerl.DoesNotExist:
            messages.error(request, "Invalid credentials")
            return redirect('signin-owner')


    return render(request, 'loginowner.html')




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
        return redirect('payment')
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
        return redirect('payment')
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
        return redirect('payment')
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
        # Redirect to contact details page with the current date
        return redirect('home')

    return render(request, 'contact.html')

def contact1(request):
    if request.method == "POST":
        contactname = request.POST.get('contactname', '')
        contactemail = request.POST.get('contactemail', '')
        contactnumber = request.POST.get('contactnumber', '')
        contactmsg = request.POST.get('contactmsg', '')
        tosend = contactmsg + '.....................................................This is just an acknowledgement'
        contact = ContactUs(name=contactname, email=contactemail, phone_number=contactnumber, message=contactmsg)
        contact.save()
        send_mail(
            'Thank you for contacting Rental System',
            tosend,
            'surajkumar.sk.pika.0807@gmail.com',
            [contactemail],
            fail_silently=False,
        )
        # Redirect to contact details page with the current date
        return redirect('home-owner')

    return render(request, 'contact1.html')


def handle(request):
    contacts = Contact.objects.filter()
    return render(request, 'handle.html', {'contacts': contacts})

def handle1(request):
    contactsus = ContactUs.objects.filter()
    return render(request, 'handle1.html', {'contactsus': contactsus})

def OwnerInfo(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        business_na = request.POST['business_na']
        business_address = request.POST['business_address']
        business_ph = request.POST['business_ph']

        owner = VehicleShop(
            name=name,
            phone=phone,
            email=email,
            address=address,
            business_na=business_na,
            business_address=business_address,
            business_ph=business_ph,
        )
        owner.save()

        return redirect('docs')

    return render(request, 'OwnerInfo.html')


def docs(request):
    if request.method == 'POST':
        aadhar_card = request.FILES.get('aadhar-card')
        pan_card = request.FILES.get('pan-card')
        business_license = request.FILES.get('business-license')
        vehicle_proof_documents = request.FILES.get('vehicle-proof-documents')
        vehicle_insurance_documents = request.FILES.get('vehicle-insurance-documents')


        OwnerDocuments.objects.create(
            aadhar_card=aadhar_card,
            pan_card=pan_card,
            business_license=business_license,
            vehicle_proof_documents=vehicle_proof_documents,
            vehicle_insurance_documents=vehicle_insurance_documents
        )

        return redirect('home-owner')

    return render(request, 'OwnerDocs.html')


def ownerbankdetails(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        bank_name = request.POST['bank-name']
        branch_name = request.POST['branch-name']
        account_number = request.POST['account']
        ifsc_code = request.POST['ifsc']
        BankDetails.objects.create(
            name=name,
            phone=phone,
            bank_name=bank_name,
            branch_name=branch_name,
            account_number=account_number,
            ifsc_code=ifsc_code
        )
        return redirect('vehicle-pdfs')

    return render(request, 'OwnerBankDetails.html')

def OwnerVehicleDetails(request):
    return render(request, 'OwnerVehicleDetails.html')







