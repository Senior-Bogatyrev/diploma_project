from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE)
    
    country = models.CharField(blank=True, null=True, max_length=50)

    city = models.CharField(blank=True, null=True, max_length=50)
    
    date_of_birth = models.DateField(blank=True, null=True)

    photo = models.ImageField(upload_to='users/%Y/%m/%d/', 
                              blank=True)

    def __str__(self):
        return f'Profile of {self.user.username}'