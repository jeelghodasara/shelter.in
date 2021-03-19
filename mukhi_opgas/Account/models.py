from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class Register(models.Model):
    
class User_Registration(models.Model):
    # user=models.ForeignKey(User, on_delete=models.CASCADE)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    ut=(
        ("Guest","guest"),
        ("Owner","Owner")
    )
    user_type=models.CharField(max_length=20,choices=ut,default="Guest")
    mobile_no=models.CharField(max_length=12)
    