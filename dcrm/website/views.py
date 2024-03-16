from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecord
from .models import Record


def home(request):
    # check to see logging in
    records = Record.objects.all()

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
    else:
        return render(request, 'home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out! ")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:

        # lookup record
        record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': record})

    else:
        messages.success(request, "You must be logged in to view! ")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:

        # delete record
        record_it = Record.objects.get(id=pk)
        record_it.delete()
        messages.success(request, "Record deleted successfully! ")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to delete record! ")
        return redirect('home')


def add_record(request):
    form = AddRecord(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added..")
                return redirect('home')

        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, "You must be logged in add record..")
        return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        to_update = Record.objects.get(pk=pk)
        form = AddRecord(request.POST or None, instance=to_update)
        if request.method == 'POST':
            form.is_valid()
            form.save()
            messages.success(request, "Record is updated")
            return redirect('home')
        else:
            return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, "You must be logged in add record..")
        return redirect('home')