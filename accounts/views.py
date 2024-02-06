from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        # Checking if user is valid
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/')

        else:
            return redirect('accounts:login')
    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'accounts/login.html')





def signout(request):
    logout(request)
    return redirect('accounts:login')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            return HttpResponse('Passwords do not match')
        user = User.objects.create_user(username=username, email=email, password=password)
        
        user.save()
        
        print('lineeeee:', user)


        if not user:
            return HttpResponse('Something went wrong')
        return redirect('accounts:login')
    return render(request, 'accounts/register.html')
