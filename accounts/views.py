from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def loginUser(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
            # A backend authenticated the credentials
        else:
            return render(request, 'login.html')
            # No backend authenticated the credentials
    return render(request, 'login.html')


def logoutuser(request):
    logout(request)
    return redirect('/accounts/login')


def signupuser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Username already in use')
            return render(request, 'signup.html')
        else:
            user = User.objects.create_user(
                username=username, password=password)
            return redirect('/accounts/login')
    return render(request, 'signup.html')
