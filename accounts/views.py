from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            return HttpResponse(status=404)
        authenticate(request, username=username, password=password)
        return redirect('base:base')
    return render(request, template_name='accounts/login.html')


def signout(request):
    return redirect('accounts:signup')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            return HttpResponse('Passwords do not match')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_active = False
        user.save()


        if not user:
            return HttpResponse('Something went wrong')
        return redirect('accounts:login')
    return render(request, 'accounts/register.html')
