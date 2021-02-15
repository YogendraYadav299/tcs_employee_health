from django.shortcuts import render,redirect
from health.forms import CustomRegisterForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from health.models import HealthReport,EmployeeDevice

import requests

# Create your views heredef register(request):
'''

return render('health/register.html',user_form)'''
def register_page(request):
    user = request.user
    if user.id:
        return redirect('dashboard')

    form=CustomRegisterForm()
    if request.method == "POST":
        form=CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account is created for '+ user)

            return redirect('login')
    context={'form':form}
    return render(request,'health/register.html', context)


def login_page(request):
    user = request.user
    if user.id:
        return redirect('dashboard')

    if request.method == "POST":
        email=request.POST.get('email')
        password =request.POST.get('password')
        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)
            if user is not None:
                login(request,user)
                return redirect("dashboard")
            else:
                messages.warning(request,"Incorrect Email or Password")
                pass
        except:
            messages.info(request, "Incorrect Email or  Password")

    return render(request, 'health/login.html')

@login_required
def dashboard_page(request):
    user = request.user
    if user.is_superuser:
        devices = EmployeeDevice.objects.all()
    else:
        devices = EmployeeDevice.objects.filter(user=user)

    data = []
    for device in devices:
        device_data = {}
        device_data["device"] = device
        device_data["health_data"] = HealthReport.objects.filter(device=device).first()

        data.append(device_data)
    return render(request,'health/dashboard.html',context={"data":data})

def logout_page(request):
    logout(request)
    return redirect('login')

