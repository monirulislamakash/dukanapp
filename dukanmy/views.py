from django.shortcuts import render
from django.core.mail import send_mail
import random
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
        return render(request,"login.html",{'successfully':'we will get back to you soon'})
    return render(request,"login.html")