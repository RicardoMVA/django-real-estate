from django.shortcuts import render, redirect

from django.contrib import messages


def register(request):
    if request.method == 'POST':
        # register user
        messages.error(request, 'Testing error message')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        # login user
        return render(request, 'accounts/login.html')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
