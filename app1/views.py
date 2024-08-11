from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='loginpage')
def create(request):
    if request.method=="POST":
        pname=request.POST.get("pname")
    return render(request,'create.html')


def home(request):
    return render(request,'home.html')

def loginv(request):
    if request.user.is_authenticated:
        return redirect("homepage")
    if request.method=="POST":
        username=request.POST.get("uname")
        password=request.POST.get("passw")
        print(username,password)
        result=authenticate(request,username=username,password=password)
        if result is not None:
            login(request,result)
            if request.user.is_superuser:
                return redirect('/admin')
            else:
                return redirect('profilepage')
        else:
            return redirect("loginpage")
    return render(request,'login.html')

@login_required(login_url='loginpage')
def profile(request):
    if request.user.is_superuser:
        return redirect('/admin')
    return render(request,'profile.html')

def register(request):
    if request.method=="POST":
        a=request.POST.get("uname")
        b=request.POST.get("fname")
        c=request.POST.get("lname")
        d=request.POST.get("mail")
        e=request.POST.get("passw")
        f=request.POST.get("cpass")
        if User.objects.filter(username=a).exists():
            return redirect('registerpage')
        if len(e)<8:
            return redirect('registerpage')
        if (e!=f):
            return redirect('registerpage')
        obj=User.objects.create_user(username=a,first_name=b,last_name=c,email=d,password=e)
        obj.save()
        return redirect('loginpage')
    return render(request,'register.html')

def single(request):
    return render(request,'single.html')

def logoutv(request):
    logout(request)
    return redirect('loginpage')