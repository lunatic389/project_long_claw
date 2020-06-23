from django.db import models
from django.forms import ModelForm

BLOOD_TYPE = [
    ('A+'), ('A-'),
    ('B+'), ('B-.'),
    ('AB+'), ('AB-'),
    ('O+'), ('O-'),
]

class Info(models.Model):
    name = models.CharField(max_length=100)
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE)
    resident_state = models.CharField(max_length=2)
    birth_date = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=10)
