from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from Account.models import User_Registration


# Create your models here.

class Property(models.Model):
    owner=models.ForeignKey(User_Registration, null=True, on_delete=models.SET_NULL)
    p_name = models.CharField(max_length=100)
    city=(
        ('Rajkot','Rajkot'),
        ('Ahmedabad','Ahmedabad'),
        ('Vadodara','Vadodara'),
    )
    p_city = models.CharField(max_length=50, blank=True, null=True, choices=city)
    state=(
        ('Gujarat','Gujarat'),
        ('Rajasthan','Rajasthan'),
        ('Panjab','Panjab'),
        ('Hariyana','Hariyana'),
    )
    p_state = models.CharField(max_length=50, choices=state)
    email = models.EmailField(max_length=254)
    area_code = models.IntegerField(default=91)
    phone = models.CharField(max_length=12)
    propertytype=(
        ('PG','PG'),
        ('Apartment','Apartment'),
    )
    p_type = models.CharField(max_length=50, choices=propertytype)
    p_address = models.CharField(max_length=1024)
    execting_cus = models.BooleanField(default=False)
    p_price = models.IntegerField(default=0)
    p_time_area = models.CharField(max_length=50)
    p_rooms_available = models.IntegerField(default=1) 
    p_floor_no = models.IntegerField(default=0)
    p_sharing_member = models.IntegerField(default=1)
    tenents=(
        ('Boys','Boys'),
        ('Girls','Girls'),
        ('Family','Family')
    )
    tenants_preffered = models.CharField(max_length=50, choices=tenents)
    photo = models.ImageField(null=True, upload_to='p_images')
    p_amanities = models.CharField(max_length=200)
    house_rules = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
