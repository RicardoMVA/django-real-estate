from django.shortcuts import render, redirect

from django.contrib import messages, auth

# imports 'User' model needed for authentication
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        # stores passed info from form
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check if passwords match
        if password == password2:
            # check if username is already in use inside DB
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username is already in use')
                return redirect('register')
            else:
                # check if email is already in use inside DB
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'This email is already in use')
                    return redirect('register')
                else:
                    # proceed with registration

                    # create new user
                    user = User.objects.create_user(
                        username=username,
                        password=password,
                        email=email,
                        first_name=first_name,
                        last_name=last_name)

                    # store info into DB
                    user.save()

                    # login immediately after registration
                    auth.login(request, user)

                    messages.success(
                        request, 'Register successful, you are logged in')
                    return redirect('index')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        # stores passed 'username' and 'password' from form
        username = request.POST['username']
        password = request.POST['password']

        # checks if the user exists in DB
        user = auth.authenticate(
            username=username,
            password=password)

        # if the user doesn't exists, 'user' returns 'none'
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

        return render(request, 'accounts/login.html')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Logged out')
        return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
