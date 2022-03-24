from email import message
import email
from django.shortcuts import redirect, render
from .models import *
from random import randint
# Create your views here.
def IndexPage(request):
    return render(request,"app/index.html")

def AboutPage(request):
    return render(request,"app/about.html")

def ServicePage(request):
    return render(request,"app/service.html")

def ProjectPage(request):
    return render(request,"app/project.html")

def ContactPage(request):
    return render(request,"app/contact.html")
    
def SignupPage(request):
    return render(request,"user/signup.html")


def RegisterUser(request):
    if request.POST["role"]=="Housekeeper":
        role = request.POST['role']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
    
        user = UserMaster.objects.filter(email=email)
        
        if user:
            message = "User already exist...."
            return render(request,"user/signup.html",{'msg':message})
        else:
            if password==cpassword:
                otp = randint(100000,999999)
                newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                newhousekeeper = Housekeeper.objects.create(user_id=newuser,firstname=fname,lastname=lname)
                return render(request,"user/otpverify.html",{'email':email})
            else:
                message = " Password & Confirm password didnot match..."
                return render(request,"user/signup.html",{'msg':message})
    else:
        role = request.POST['role']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
    
        user1 = UserMaster.objects.filter(email=email)
        
        if user1:
            message = "User already exist...."
            return render(request,"user/signup.html",{'msg':message})
        else:
            if password==cpassword:
                otp = randint(100000,999999)
                newuser1 = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                newcustomer = Customer.objects.create(user_id=newuser1,firstname=fname,lastname=lname)
                return render(request,"user/otpverify.html",{'email':email})
            else:
                message = " Password & Confirm password didnot match..."
                return render(request,"user/signup.html",{'msg':message})
def OtpPage(request):
    return render(request,"user/otpverify.html")
def OtpVerify(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])
    
    user = UserMaster.objects.get(email=email)
    
    
    if user:
        if user.otp == otp:
            message = "OTP verified Successfully...."
            return render(request,"user/login.html",{'msg':message})        
        else:
            message = "OTP is incorrect...."
            return render(request,"user/otpverify.html",{'msg':message})
    else:
        return render(request,"user/signup.html")
def LoginPage(request):
    return render(request,"user/login.html")

def LoginUser(request):
    if request.POST['role']=="Housekeeper":
        email = request.POST['email']
        password = request.POST['password']
        
        user = UserMaster.objects.get(email=email)
        if user:
            if user.password==password and user.role=="Housekeeper":
                houskeeper = Housekeeper.objects.get(user_id =user)
                request.session['id']=user.id
                request.session['role'] =user.role
                request.session['firstname'] =houskeeper.firstname
                request.session['lastname'] =houskeeper.lastname
                request.session['email'] =user.email
                return redirect('index')
            else:
                message = "Please Enter correct Password..."
        return render(request,"user/login.html",{'msg':message})

    elif request.POST['role']=="Customer":
        email = request.POST['email']
        password = request.POST['password']
        
        user = UserMaster.objects.get(email=email)
        if user:
            if user.password==password and user.role=="Customer":
                customer = Customer.objects.get(user_id =user)
                request.session['id']=user.id
                request.session['role'] =user.role
                request.session['firstname'] =customer.firstname
                request.session['lastname'] =customer.lastname
                request.session['email'] =user.email
                return redirect('index')
            else:
                message = "Please Enter correct Password..."
        return render(request,"user/login.html",{'msg':message})

    
    else:
        message = "User doesnot exist..."
        return render(request,"user/login.html",{'msg':message})

        
        