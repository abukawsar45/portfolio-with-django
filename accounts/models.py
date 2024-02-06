from django.contrib.auth.models import User
from django.db import models



class Profile(models.Model):
    photo = models.ImageField(upload_to='profile_pics')
    address = models.CharField(max_length=250, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verify_key = models.CharField(max_length=10, blank=True)
    


    def __str__(self):
        return self.user.username
