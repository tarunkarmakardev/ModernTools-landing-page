from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:profile')
        else:
            messages.error(request, "Invalid credentials!")
            return redirect('accounts:login')

    if 'registered' in request.GET:
        messages.success(request, "Account created! Login now")

    if 'pagerequireslogin' in request.GET:
        messages.info(request, "This page requires you to login!")

    context = {}

    return render(request, "accounts/login.html", context)


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('accounts:profile')
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=email).exists():
                messages.error(request, "Email ID already exists!")
                return redirect('accounts:register')
            else:
                user = User.objects.create_user(
                    first_name=firstname, last_name=lastname, email=email, username=email, password=password)
                user.save()
                return redirect('/accounts/login/?registered')

        else:
            messages.error(request, "Password didn't match!")
            return redirect('accounts:register')

    context = {}

    return render(request, "accounts/register.html", context)


def logoutUser(request):
    logout(request)
    return redirect('main:home')


@login_required(login_url='/accounts/login/?pagerequireslogin')
def profile(request):

    context = {}
    return render(request, 'accounts/profile.html', context)
