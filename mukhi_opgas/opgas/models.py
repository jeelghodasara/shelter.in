from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from Account.models import User_Registration


# Create your models here.

class Property(models.Model):
    # P_Id=models.AutoField

    owner=models.ForeignKey(User_Registration, null=True, on_delete=models.SET_NULL)
    p_name = models.CharField(max_length=100)
    country={
        ('India','India'),
        ('Usa','Usa'),
        ('Australiya','Australiya')
    }
    state=(
        ('Gujarat','Gujarat'),
        ('Rajasthan','Rajasthan'),
        ('Panjab','Panjab'),
        ('Hariyana','Hariyana'),
    )
    city=(
        ('Rajkot','Rajkot'),
        ('Ahmedabad','Ahmedabad'),
        ('Vadodara','Vadodara'),
    )
    p_country=models.CharField(choices=country, max_length=50, null=True)
    p_state = models.CharField(choices=state, max_length=50, null=True)
    p_city = models.CharField(choices=city, max_length=50, null=True)
 
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
    photo = models.ImageField(max_length=2000,  upload_to='p_images')
    photo1 = models.ImageField(max_length=2000, upload_to='p_images')

    photo2 = models.ImageField(max_length=2000, upload_to='p_images')
    photo3 = models.ImageField(max_length=2000,upload_to='p_images')

    photo4 = models.ImageField(max_length=2000, upload_to='p_images')


    p_amanities = models.CharField(max_length=200)
    house_rules = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)



class Booking(models.Model):
    Booking_Id=models.AutoField
    user_id = models.IntegerField(default=0 )
    owner_id = models.IntegerField(default=0)
    Due_date= models.DateField()
    p_name= models.CharField(max_length=100)
    p_type = models.CharField(max_length=100)
    p_address = models.CharField(max_length=100)
    p_state = models.CharField(max_length=100)
    Check_IN= models.DateTimeField()
    Check_OUT = models.DateTimeField()
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    tel=models.CharField(max_length=12,default=None,null=True)
    Phone_no=models.CharField(max_length=15,default=None,null=True)
    People=models.IntegerField(default=None,null=True)
    p_price = models.IntegerField(default=None,null=True)
    T_price = models.IntegerField(default=None,null=True)
    F_price = models.IntegerField(default=None,null=True)
    Days = models.IntegerField(default=None,null=True)
