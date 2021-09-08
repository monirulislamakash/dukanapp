from django.shortcuts import render,redirect
from django.core.mail import send_mail
import random
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
otpuser=[]
def login(request):
    if request.method=="POST":
        otpmail=request.POST.get("otpemail")
        otpnum=str(random.randint(10000000, 99999999))
        problem="Dukan OTP "
        print(otpnum)
        send_mail(
            problem,
            "Your OTP is :"+otpnum,
            'monirulislamakash18@gmail.com',
            [otpmail],
            fail_silently=False,
        )
        try:
            newpass=otpnum
            u = User.objects.get(username=otpmail)
            u.set_password(newpass)
            u.save()
            otpuser.append(otpmail)
            return redirect(otp)
        except User.DoesNotExist:
            user=User.objects.create_user(username=otpmail,password=otpnum)
            return render(request,"login.html")
    return render(request,"login.html")
def index(request):
    if request.user.is_authenticated:
        return render(request,"index.html")
    return redirect(login)
def otp(request):
    email=otpuser[0]
    passw=request.POST.get("password")
    if request.method=="POST":
       user=auth.authenticate(username=email,password=passw)
       if user is not None:
            auth.login(request,user)
            return redirect(index) 
       else:
            return render(request,"otp.html",{'error':"Invalide User Password"})
    print(email,passw)
    return render(request,"otp.html")