from django.conf import settings
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.models import Profile
from django.contrib.auth.decorators import login_required

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
        user.is_active=False
        user.save()
        Profile.objects.create(user=user, verify_key=123456)
        send_verification_email(username, email)
        

        if not user:
            return HttpResponse('Something went wrong')
        return redirect('accounts:login')
    return render(request, 'accounts/register.html')


def activate_account(request):
    verify_key = request.GET.get('verify_key')
    profile = Profile.objects.filter(verify_key=verify_key).last()
    profile.user.is_active = True
    profile.user.save()
    return redirect('accounts:login')



# send email verification message
def send_verification_email (username, email) : 
    subject = 'welcome my new website, Please confirm the request!!!'
    message = f'Hi {username}, thank you for registering in my new website.\nYour verification link: http://127.0.0.1:8000/accounts/verify-account/?verify_key=123456'
    email_from = 'no-reply@kawsar.com'
    recipient_list = [email]
    send_mail( subject, message, email_from, recipient_list )




@login_required(login_url="/accounts/login/")
def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    context = {
        'profile': profile
    }
    return render(request, template_name='accounts/profile.html', context=context)  