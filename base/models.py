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
state_select=[('AL','AL'),
    ('AK','AK'),
    ('AZ','AZ'),
    ('AR','AR'),
    ('CA','CA'),
    ('CO','CO'),
    ('CT','CT'),
    ('DE','DE'),
    ('DC','DC'),
    ('FL','FL'),
    ('GA','GA'),
    ('HI','HI'),
    ('ID','ID'),
    ('IN','IN'),
    ('IA','IA'),
    ('KS','KS'),
    ('KY','KY'),
    ('LA','LA'),
    ('ME','ME'),
    ('MD','MD'),
    ('MA','MA'),
    ('MI','MI'),
    ('MN','MN'),
    ('MS','MS'),
    ('MO','MO'),
    ('MT','MT'),
    ('NE','NE'),
    ('NV','NV'),
    ('NH','NH'),
    ('NJ','NJ'),
    ('NM','NM'),
    ('NY','NY'),
    ('NC','NC'),
    ('ND','ND'),
    ('OH','OH'),
    ('OK','OK'),
    ('OR','OR'),
    ('PA','PA'),
    ('RI','RI'),
    ('SC','SC'),
    ('SD','SD'),
    ('TN','TN'),
    ('TX','TX'),
    ('UT','UT'),
    ('VT','VT'),
    ('VA','VA'),
    ('WA','WA'),
    ('WV','WV'),
    ('WI','WI'),
    ('WY','WY'),
    ]


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    blood_type= models.CharField(max_length=3,choices=Blood_type,default='O+')
    resident_state=models.CharField(max_length=2,choices=state_select,default='AL')
    date_of_birth=models.DateField(blank=True,null=True)
    phone_number=models.CharField(max_length=10)
    registered_as=models.CharField(max_length=7,choices=account_type,default='Donar')
    requested = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email
