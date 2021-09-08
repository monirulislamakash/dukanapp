from django.shortcuts import render,redirect
from django.core.mail import send_mail
import random
from django.contrib.auth.models import User
# Create your views here.
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
        except User.DoesNotExist:
            user=User.objects.create_user(username=otpmail,password=otpnum)
            return render(request,"login.html")
    return render(request,"login.html")
def index(request):
    return render(request,"index.html")