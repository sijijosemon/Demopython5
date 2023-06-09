from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
# Create your views here.
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login

def index(request):
    return render(request,"index.html")
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username, password)
        user.save()
        return redirect('login')
    return render(request, "register.html")
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('loggedin')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def loggedin(request):

    return render(request,"loggedin.html")
def regform(request):
    if request.method=='POST':
         f_name = request.POST['firstname']
         l_name = request.POST['lastname']
         age = request.POST['age']
         male = request.POST['male']
         female = request.POST['female']
         others = request.POST['other']
         country_code = request.POST['country code']
         phone = request.POST['phone']
         address = request.POST['address']
         email = request.POST['email']
         user= User.objects.create_user(f_name,l_name,age,male,female,others,country_code,phone,address,email)
         user.save()
         return HttpResponse("Order Confirmed")
    return render(request,"regform.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
def confirm(request):
    return redirect('/')