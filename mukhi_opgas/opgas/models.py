from django.db import models

# Create your models here.
    
class Property(models.Model):
    p_name = models.CharField(max_length=100)
    p_city = models.CharField(max_length=50)
    p_state = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    area_code = models.IntegerField()
    phone = models.CharField(max_length=12)
    p_type = models.CharField(max_length=50)
    p_address = models.CharField(max_length=1024)
    execting_cus = models.BooleanField()
    p_price = models.IntegerField()
    p_time_area = models.CharField(max_length=50)
    p_rooms_available = models.IntegerField() 
    p_floor_no = models.IntegerField()
    p_sharing_member = models.IntegerField()
    tenants_preffered = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='p_images')
    p_amanities = models.CharField(max_length=200)
    house_rules = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
