from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

def home(request):
    return render(request, 'home.html')

def viewRem(request, id):
    viewRem = Setreminder.objects.get(id = id)
    return render(request, 'view.html', {'viewRem': viewRem})

def viewData(request):
    setReminder = Setreminder.objects.all()
    return render(request, 'viewData.html', {'setReminder': setReminder})

def setReminder(request):
    setReminder = Setreminder.objects.all()
    if request.method == 'POST':
        date = request.POST.get('date')
        subject = request.POST.get('subject')
        description = request.POST.get('description')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        sms = request.POST.get('sms')

        user = Setreminder.objects.create(
            date = date,
            subject = subject,
            description = description,
            email = email,
            contact = contact,
            sms = sms
        )
        user.save()
        # return redirect('/')

    return render(request, 'set.html', {'setReminder': setReminder})

def updateReminder(request):
    setReminder = Setreminder.objects.all()
    return render(request, 'update.html', {'setReminder': setReminder})

def deleteReminder(request):
    setReminder = Setreminder.objects.all()
    return render(request, 'delete.html', {'setReminder': setReminder})

def delete_reminder(request, id):
    queryset = Setreminder.objects.get(id=id)
    queryset.delete()
    return redirect('deleteRem')

def update_reminder(request, id):
    queryset = Setreminder.objects.get(id = id)
    if request.method == 'POST':
        date = request.POST.get('date')
        subject = request.POST.get('subject')
        description = request.POST.get('description')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        sms = request.POST.get('sms')

        queryset.date = date
        queryset.subject = subject
        queryset.description = description
        queryset.email = email
        queryset.contact = contact
        queryset.sms = sms

        queryset.save()
        return redirect('updateRem')
    
    return render(request, 'updateData.html', {'upRem': queryset})

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username!!')
            return redirect('/login/')

        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid/Incorrect Username or Password')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/')

    return render(request, 'login.html')

def log_out(request):
    logout(request)
    return redirect('/')

def sign_up(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.error(request, 'This username is already exist')
            return redirect('/signup/')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        messages.info(request, 'Account created Successfulyy!!')
        return redirect('/login/')

    return render(request, 'signup.html')