from django.contrib import admin
from .models import Property,Booking
# Register your models here.

@admin.register(Property)
class Property_view_admin(admin.ModelAdmin):
    fields= ('owner','p_name','p_city','p_state','email','area_code','phone','p_type','p_address','execting_cus','p_price','p_time_area','p_rooms_available','p_floor_no','p_sharing_member','tenants_preffered','photo','photo1','photo2','photo3','photo4','p_amanities','house_rules')

admin.site.register(Booking)
