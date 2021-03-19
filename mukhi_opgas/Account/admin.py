from django.contrib import admin
from .models import User_Registration
# Register your models here.
@admin.register(User_Registration)
class userregestratuin(admin.ModelAdmin):
    list=[all]