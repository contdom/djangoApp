from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth.models import auth    # logout
from django.contrib.auth import authenticate # login
from django.contrib.auth.decorators import login_required

from .models import Record 

# Homepage

def home(request):
    return render(request, 'crudapp/index.html')

# Register a new user

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-login')

    context = {'form': form}
    return render(request, 'crudapp/register.html', context=context)

# log in a user

def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password) 

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')

    context = {'form': form}
    return render(request, 'crudapp/my-login.html', context=context)

# dashboard

@login_required(login_url='my-login')  # Ensure user is logged in to access the dashboard
def dashboard(request):
    my_records = Record.objects.all()
    context = {'records': my_records}
    return render(request, 'crudapp/dashboard.html', context=context)

# create a record

@login_required(login_url='my-login')  # Ensure user is logged in to access the dashboard
def create_record(request):
    
    form = CreateRecordForm()
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'crudapp/create-record.html', context=context)

# log out a user

def user_logout(request):
    auth.logout(request)
    return redirect('my-login')  # Redirect to the login page after logout