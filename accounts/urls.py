from django.urls import path
from accounts.views import *

app_name = 'accounts'
urlpatterns = [
    path('login/', signin, name='login'),
    path('logout/', signout, name='logout'),
    path('register/', signup, name='register'),
    path('profile/', profile, name='profile'),
    path('verify-account/', activate_account, name='activate_account')
]