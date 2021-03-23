from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Property,User
from .forms import Property_form
from .forms import Property_form2
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required
def Base_pgindex(request):
    return render(request, "pgindex.html")

# @login_required
def pgindex(request):
    user_name = None
    if login_required == True:
        currentuser = request.user
        user_name=currentuser.id
    else:
        user_name=None
    # user_id=None
    # if login_required == True:
    #     current_user=request.user
    #     user_id=current_user.id
    # else:
    #     user_id=None

    # pro1=Property()
    # pro1.p_name="Fortune Hotel"
    # pro1.p_city="Rajkot"
    # pro1.p_floor="25"
    # pro1.p_price="5000"
    # pro1.p_bhk="3 BHK"
    # pro1.photo="Fortune.jpg"

    # pro2=Property()
    # pro2.p_name="VILLA"
    # pro2.p_city="Rajkot"
    # pro2.p_floor="3"
    # pro2.p_price="1500000"
    # pro2.p_bhk="5 BHK"
    # pro2.p_img="Fortune.jpg"

    # pro3=Property()
    # pro3.p_name="PG"
    # pro3.p_city="Ahamdabad"
    # pro3.p_floor="10"
    # pro3.p_price="6500"
    # pro3.p_bhk="3 BHK"
    # pro3.p_img="Fortune.jpg"

    prope=Property.objects.all()

    # props1=[]
    # length=len(prope)
    # for i in range(length):
    #     props1.append(i)
    
    
    pro4=Property()
    pro4.p_name="Guest House"
    pro4.p_city="Surat"
    pro4.p_floor="20"
    pro4.p_price="2000"
    pro4.p_bhk="2 BHK"
    pro4.p_img="Fortune.jpg"

    pro5=Property()
    pro5.p_name="Vrundavan Resort"
    pro5.p_city="Rajkot"
    pro5.p_floor="0"
    pro5.p_price="2000/Hr"
    pro5.p_bhk="0"
    pro5.p_img="Fortune.jpg"

    pro6=Property()
    pro6.p_name="Jay Motels"
    pro6.p_city="Vadodara"
    pro6.p_floor="2"
    pro6.p_price="15000/hr"
    pro6.p_bhk="5 BHK"
    pro6.p_img="Fortune.jpg"

    pro7=Property()
    pro7.p_name="Jaygirnar Hotel"
    pro7.p_city="Jamnagar"
    pro7.p_floor="7"
    pro7.p_price="2000/day"
    pro7.p_bhk="1 BHK"
    pro7.p_img="Fortune.jpg"

    pro8=Property()
    pro8.p_name="Guest House"
    pro8.p_city="Surat"
    pro8.p_floor="20"
    pro8.p_price="2000"
    pro8.p_bhk="2 BHK"
    pro8.p_img="Fortune.jpg"

    pro9=Property()
    pro9.p_name="Guest House"
    pro9.p_city="Surat"
    pro9.p_floor="20"
    pro9.p_price="2000"
    pro9.p_bhk="2 BHK"
    pro9.p_img="Fortune.jpg"

    # props1=[pro1,pro2,pro3]
    props2=[pro4,pro5,pro6]
    props3=[pro7,pro8,pro9]
    context={'user_name':user_name, 'props1':prope, 'props2':props2, 'props3':props3}

    return render(request, 'pgindex.html', context)



# @login_required
def Add_property(request):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     raise Http404

    if request.method == "POST":
        # fm=Property_form2(request.POST)
        # if fm.is_valid():
        data=Property()
        p_city=request.POST.get('p_city')
        p_name=request.POST.get('p_name')
        p_state=request.POST.get('p_state')
        email=request.POST.get('email')
        area_code=request.POST.get('area_code')
        phone=request.POST.get('phone')
        p_type=request.POST.get('p_type')
        p_address=request.POST.get('p_address')
        # execting_cus=request.POST.get('execting_cus')
        p_price=request.POST.get('p_rent')
        p_time_area=request.POST.get('p_time_area')
        p_rooms_available=request.POST.get('p_rooms_available')
        p_floor_no=request.POST.get('p_floor_no')
        p_sharing_member=request.POST.get('p_sharing_member')
        tenants_preffered=request.POST.get('tenants_preffered')
        p_amanities=request.POST.getlist('p_amenities')
        house_rules=request.POST.getlist('p_house_rules')
        images=request.FILES.getlist('Images')
    
        # photo = Property_form(request.POST, request.FILES)
        data.p_name=p_name
        data.p_city=p_city
        data.p_state=p_state
        data.email=email
        data.area_code=area_code
        data.phone=phone
        data.p_type=p_type
        data.p_address=p_address
        # data.execting_cus=execting_cus
        data.p_price=p_price
        data.p_time_area=p_time_area
        data.p_rooms_available=p_rooms_available
        data.p_floor_no=p_floor_no
        data.p_sharing_member=p_sharing_member
        data.tenants_preffered=tenants_preffered
        data.p_amanities=p_amanities
        data.house_rules=house_rules
        
        for img in images:
            data.photo=img
            data.save()
        
        return redirect("/")
    # else:
    #     messages.WARNING("Invalid data")
        # fm=Property_form2()
        # image_form = Property_form()
        # img = Property.objects.all()
# {'image_form': image_form, 'fm': fm}
    return render(request, 'mysite/addproperty.html')
    
        
        

        