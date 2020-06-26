from django.db import models
from django.contrib.auth.models import User


# Create your models here.

Blood_type=[('A+','A+'),
    ('B+','B+'),
    ('AB+','AB+'),
    ('O+','O+'),
    ('O-','O-'),
    ('A-','A-'),
    ('B-','B-'),
    ('AB-','AB-')]

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    blood_type= models.CharField(max_length=10,choices=Blood_type,default='O+')
    resident_state=models.CharField(max_length=2)
    dob=models.DateField(blank=True,null=True)
    phone_number=models.CharField(max_length=10)

    def __str__(self):
        return self.user.username
