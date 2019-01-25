from django.shortcuts import render, redirect


def register(request):
    if request.method == 'POST':
        # register user

    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        # login user
 
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
