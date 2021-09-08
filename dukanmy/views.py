from django.shortcuts import render,redirect
from django.core.mail import send_mail
import random
from django.contrib.auth.models import User
# Create your views here.
def login(request):
    if request.method=="POST":
        problem="Dukan OTP "
        otpmail=request.POST.get("otpemail")
        otpnum=str(random.randint(100000, 999999))
        print(otpnum)
        send_mail(
            problem,
            "Your OTP is :"+otpnum,
            'monirulislamakash18@gmail.com',
            [otpmail],
            fail_silently=False,
        )
        try:
            user=User.objects.get(username=otpmail)
            user.set_password(otpmail)
            user.save()
        except User.DoesNotExist:
            user=User.objects.create_user(username=otpmail,password=otpnum)
    return render(request,"login.html")