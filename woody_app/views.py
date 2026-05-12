from django.shortcuts import render,redirect
from .models import Orders
import datetime as dt
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contacts(request):
    return render(request,'contact.html')

def projects(request):
    return render(request,'project.html')

def featutes(request):
    return render(request,'feature.html')

def services(request):
    return render(request,'service.html')

def quotes(request):
    return render(request,"quote.html")

@login_required
def booking(request):
    if request.method=="POST":
        name=request.POST['uname']
        email=request.POST['umail']
        mobile=request.POST['mobile']
        service=request.POST['service']
        budget=request.POST['budget']
        message=request.POST['note']

        row=Orders.objects.create(name=name,email=email,mobile=mobile
        ,service=service,budget=budget,note=message)
        row.save()
       
        bid=request.user.username+str(mobile[0:3])+service[0:3]
        cur_date=dt.datetime.now()
        bdate=cur_date.strftime("%d-%m-%Y %H:%M")
        pickup=cur_date+dt.timedelta(days=7)
        pdate=pickup.strftime("%d-%m-%Y %H:%M")
        drop=pickup+dt.timedelta(days=10)
        ddate=drop.strftime("%d-%m-%Y %H:%M")

        data={"bid":bid,"bdate":bdate,"cname":name,"cnumber":mobile,
              "staken":service,"bvalue":budget,"snote":message,"pdate":pdate,"ddate":ddate}

    return render(request,"booking_info.html",data)

def teams(request):
    return render(request,'team.html')

def error(request):
    return render(request,'404.html')

def testimonials(request):
    return render(request,"testimonial.html")


def signup_view(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        c_password=request.POST["confirm_password"]

        print(username,password,c_password)

        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exists")
            return render(request,"signup.html")
        
        if not password==c_password:
            messages.error(request,"Passwords Does not Match")
            return render(request,"signup.html")
        
        user=User.objects.create_user(username=username,password=password)
        user.save()
        print("Account Created Successfully!!!")

        return redirect("login")

    return render(request,'signup.html')



def login_view(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user=authenticate(request,
                          username=username,
                          password=password)
        
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.error(request,"User Not Found.")
            return render(request,"login.html")
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    messages.success(request,"Signed Out Successfully!!!")
    return redirect("login")
