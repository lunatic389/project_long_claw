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
account_type=[('Donor','Donor'),('Patient','Patient')]

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    blood_type= models.CharField(max_length=3,choices=Blood_type,default='O+')
    resident_state=models.CharField(max_length=2)
    dob=models.DateField(blank=True,null=True)
    phone_number=models.CharField(max_length=10)
    registered_as=models.CharField(max_length=7,choices=account_type,default='Donar')

    def __str__(self):
        return self.user.username
