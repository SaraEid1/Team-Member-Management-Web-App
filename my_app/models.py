from django.db import models
from phone_field import PhoneField
from django import forms


# Create your models here.

class TeamMember (models.Model):
    # id, info (firstname, lastname, email, phone number), role
    id = models.AutoField(primary_key=True) #unique id for each team member
    firstname = models.CharField (max_length=250)
    lastname = models.CharField (max_length=250)
    email = models.EmailField (max_length=250)
    phonenumber = PhoneField(blank=True, help_text='phone number')
    role = models.CharField (max_length=100)
    #role=forms.CharField(label='Role', widget=forms.RadioSelect(choices=ROLE_CHOICES))