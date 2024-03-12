from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    # check to see logging in
    if request.method == 'POST':
        # request.body for raw json data
        username = request.POST['user_name']
        password = request.POST['password']
        # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have been Logged In")
            return redirect('home')
        else:
            messages.success(request, "Login Error! ")
            return redirect('home')

    return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out! ")
    return redirect('home')


def register_user(request):
    return render(request, 'register.html', {})
