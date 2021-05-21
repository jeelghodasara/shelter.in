import datetime
from datetime import date

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, request
from pyasn1.compat.octets import null
from datetime import datetime
from .models import Property, User, Booking
from .forms import Property_form, Userupdateform, Userupdateform1
from Account.models import User_Registration
from .forms import Property_form2
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from math import ceil


# Create your views here.

@login_required
def Base_pgindex(request):
    return render(request, "pgindex.html")


def plistpageprice(request, price=None):
    pform=User_Registration.objects.all()
    if price != None:
        p = 0

        if price == 'upto2000':
            p = 2000
        elif price == 'upto5000':
            p = 5000
        elif price == 'upto8000':
            p = 8000
        elif price == 'upto10000':
            p = 10000
        elif price == 'upto15000':
            p = 15000
        elif price == 'upto20000':
            p - 20000
        elif price == 'upto25000':
            p = 25000
        elif price == '25000&More':
            p = 25000
            prope = []
            print('a')
            prope = Property.objects.filter(p_price__gte=p)

            a = []
            print(prope)
            for i in range(len(prope)):
                prope[i].p_amanities = ((prope[i].p_amanities).replace("'", '').strip("][").split(','))
            print(len(prope))
            param = {'prope': prope}
            return render(request, "product_list_page.html", param)
        prope = []
        print('a')
        prope = Property.objects.filter(p_price__lte=p)

        a = []
        print(prope)
        for i in range(len(prope)):
            prope[i].p_amanities = ((prope[i].p_amanities).replace("'", '').strip("][").split(','))
        print(len(prope))
        param = {'prope': prope,'pform':pform}
        return render(request, "product_list_page.html", param)


def plistpagestate(request, state=None):
    pform=User_Registration.objects.all()
    if state != None:
        print('a')
        prope = Property.objects.filter(p_state=state)
        a = []
        print(prope)
        for i in range(len(prope)):
            prope[i].p_amanities = ((prope[i].p_amanities).replace("'", '').strip("][").split(','))
        print(len(prope))
        param = {'prope': prope,'pform':pform}

        return render(request, "product_list_page.html", param)


def plistpagecity(request, city=None):
    pform=User_Registration.objects.all()
    if city != None:
        print(city)
        prope = Property.objects.filter(p_city=city)
        a = []
        for i in range(len(prope)):
            prope[i].p_amanities = ((prope[i].p_amanities).replace("'", '').strip("][").split(','))

        param = {'prope': prope,'pform':pform}

        return render(request, "product_list_page.html", param)


def plistpage(request, type=None, city=None):
    pform=User_Registration.objects.all()
    if type != None:
        prope = Property.objects.filter(p_type=type)
        a = []
        for i in range(len(prope)):
            prope[i].p_amanities = ((prope[i].p_amanities).replace("'", '').strip("][").split(','))

        param = {'prope': prope,'pform':pform}

        return render(request, "product_list_page.html", param)
    elif city != None:
        prope = Property.objects.filter(p_city=city)
        a = []
        for i in range(len(prope)):
            prope[i].p_amanities = ((prope[i].p_amanities).replace("'", '').strip("][").split(','))

        
        param = {'prope': prope,'pform':pform}

        return render(request, "product_list_page.html", param)


def view_page(request, id):
    prope = Property.objects.filter(id=id)
    print(type)
    img = (prope[0].photo)
    owner = (prope[0].owner)
    p_name = (prope[0].p_name)
    p_city = (prope[0].p_city)
    p_state = (prope[0].p_state)
    email = (prope[0].email)
    area_code = (prope[0].area_code)
    phone = (prope[0].phone)
    p_type = (prope[0].p_type)
    p_address = (prope[0].p_address)
    execting_cus = (prope[0].execting_cus)
    p_price = (prope[0].p_price)
    p_time_area = (prope[0].p_time_area)
    p_rooms_available = (prope[0].p_rooms_available)
    p_floor_no = (prope[0].p_floor_no)
    p_sharing_member = (prope[0].p_sharing_member)
    tenants_preffered = (prope[0].tenants_preffered)
    photo = (prope[0].photo)
    photo1 = (prope[0].photo)
    photo2 = (prope[0].photo1)
    photo3 = (prope[0].photo2)
    photo4 = (prope[0].photo3)
    photo5 = (prope[0].photo4)

    p = []
    p_amanities = (prope[0].p_amanities).replace("'", '').strip("][").split(',')
    house_rules = (prope[0].house_rules).replace("'", '').strip("][").split(',')

    pform=User_Registration.objects.all()

    params = {'id': id, 'img': img, 'owner': owner, 'p_name': p_name, 'p_city': p_city, 'p_state': p_state,
              'email': email, 'area_code': area_code, 'phone': phone, 'p_type': p_type, 'p_address': p_address,
              'execting_cus': execting_cus, 'p_price': p_price, 'p_time_area': p_time_area,
              'p_rooms_available': p_rooms_available, 'p_floor_no': p_floor_no, 'p_sharing_member': p_sharing_member,
              'tenants_preffered': tenants_preffered, 'photo1': photo1, 'photo2': photo2, 'photo3': photo3,
              'photo4': photo4, 'photo5': photo5, 'p_amanities': p_amanities, 'house_rules': house_rules,'pform':pform}
    

    return render(request, "view_page.html", params)


# @login_required
def pgindex(request):
    user_name = None
    if login_required == True:
        currentuser = request.user  # user_id=None

        user_name = currentuser.id
    else:
        user_name = None

    # prope = Property.objects.all()
    # n = len(prope)
    # nSlides = n // 4 + ceil((n / 4) - (n // 4))
    # allpro = [[prope, range(1, len(prope)), nSlides]]
    pform=User_Registration.objects.all()

    form2 = User_Registration.objects.all()
    context = {'user_name': user_name, 'pform':pform, 'form2': form2}
    return render(request, 'pgindex.html', context)


@login_required
def Add_property(request):
    # if not request.user.is_staff or not requestaddress .user.is_superuser:
    #     raise Http404

    if request.method == "POST":
        # fm=Property_form2(request.POST)
        # if fm.is_valid():
        data = Property()
        p_city = request.POST.get('p_city')
        p_name = request.POST.get('p_name')
        p_country = request.POST.get('p_country')
        p_state = request.POST.get('p_state')
        email = request.POST.get('email')
        area_code = request.POST.get('area_code')
        phone = request.POST.get('phone')
        p_type = request.POST.get('p_type')
        p_address = request.POST.get('p_address')
        # execting_cus=request.POST.get('execting_cus')
        p_price = request.POST.get('p_rent')
        p_time_area = request.POST.get('p_time_area')
        p_rooms_available = request.POST.get('p_rooms_available')
        p_floor_no = request.POST.get('p_floor_no')
        p_sharing_member = request.POST.get('p_sharing_member')
        tenants_preffered = request.POST.get('tenants_preffered')
        p_amanities = request.POST.getlist('p_amenities')
        house_rules = request.POST.getlist('p_house_rules')
        images = request.FILES.getlist('Images')

        # photo = Property_form(request.POST, request.FILES)
        data.p_name = p_name
        data.p_city = p_city
        data.p_state = p_state
        data.p_county = p_country
        data.email = email
        data.area_code = area_code
        data.phone = phone
        data.p_type = p_type
        data.p_address = p_address
        # data.execting_cus=execting_cus
        data.p_price = p_price
        data.p_time_area = p_time_area
        data.p_rooms_available = p_rooms_available
        data.p_floor_no = p_floor_no
        data.p_sharing_member = p_sharing_member
        data.tenants_preffered = tenants_preffered
        data.p_amanities = p_amanities
        data.house_rules = house_rules
        data.owner = User_Registration.objects.get(user=request.user)
        print(images)

        # photo = Property_form(request.POST, request.FILES)
        data.p_name = p_name
        data.p_city = p_city
        data.p_state = p_state
        data.p_country=p_country
        data.email = email
        data.area_code = area_code
        data.phone = phone
        data.p_type = p_type
        data.p_address = p_address
        # data.execting_cus=execting_cus
        data.p_price = p_price
        data.p_time_area = p_time_area
        data.p_rooms_available = p_rooms_available
        data.p_floor_no = p_floor_no
        data.p_sharing_member = p_sharing_member
        data.tenants_preffered = tenants_preffered
        data.p_amanities = p_amanities
        data.house_rules = house_rules
        # user=User_Registration
        # if user:
        #     data.owner=user.pk

        print(images)
        j = 0
        for i in images:
            if j == 0:
                data.photo = i
                j += 1
            elif j == 1:
                data.photo1 = i
                j += 1
            elif j == 2:
                data.photo2 = i
                j += 1
            elif j == 3:
                data.photo3 = i
                j += 1
            elif j == 4:
                data.photo4 = i
                j += 1

        data.save()

        return redirect("/")

    return render(request, 'mysite/addproperty.html')


def Owner_dashbord(request):
    owner = User_Registration.objects.get(user=request.user)
    print(owner.id)
    pform=User_Registration.objects.all()
    context={'pform':pform}

    prope = Booking.objects.filter(owner_id=owner.id)
    a = 0
    for i in prope:
        a = a + i.F_price
    booking_no = len(prope)

    parmas = {'prope': prope, 'a': a, 'booking_no': booking_no,'pform':pform}

    return render(request, 'mysite/Owner_dashbord.html', parmas)


def Charts(request):
    return render(request, 'mysite/charts.html')


def Forgot_password(request):
    return render(request, 'mysite/forgot-password.html')

def Admin_Dashbord(request):
    pform=User_Registration.objects.all()
    context={'pform':pform}
    return render(request,'mysite/Admin_Dashbord.html',context)

@login_required
def Profile(request):
    profileform=User_Registration.objects.all()
    pform1=Userupdateform(data=request.POST, instance=request.user)
    pform2=Userupdateform1(data=request.POST)
    user=User_Registration.objects.get(user=request.user)
    data=User.objects.get(pk=request.user.id)
    if request.method == "POST":
        firstname=request.POST.get('first_name')
        lastname=request.POST.get('last_name')
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        profile_pic=request.FILES['profile_pic']

        if pform1.is_valid():
            data.first_name=firstname
            data.last_name=lastname
            data.save()
            
            user.address=address
            user.state=state
            user.city=city
            user.profilepic=profile_pic
            user.save()
            return redirect('/')
        else:
            messages.error(request,"Invalid form!!!!!")
            return redirect('Profile')

    context={'profileform':profileform,'pform1':pform1,'pform2':pform2,'user':user}
    return render(request,'mysite/Profile.html',context)


def getDifference(CheckIN, CheckOUT):
    pass


def Checkout(request, id=0):
    pform=User_Registration.objects.all()
    if request.method == "POST":
        print("---")
        firstName = request.POST.get('firstName')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        country = request.POST.get('country')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        G_firstName = request.POST.get('G_firstName')
        G_lastName = request.POST.get('G_lastName')
        G2_firstName = request.POST.get('G2_firstName')
        G2_lastName = request.POST.get('G2_lastName')
        tel = (request.POST.get('tel'))
        remarks = request.POST.get('remarks')
        CheckIN = request.POST.get('CheckIN')
        CheckOUT = request.POST.get('CheckOUT')

        # prope = User.objects.filter(username='kokkk')
        # print(prope[0].id)

        People = request.POST.get('People')

        CheckIN = (datetime.strptime(CheckIN, '%Y-%m-%dT%H:%M'))
        CheckOUT = (datetime.strptime(CheckOUT, '%Y-%m-%dT%H:%M'))
        days = abs(CheckOUT - CheckIN).days

        print('----------------------')

        quiet_room_chosen = request.POST.get('quiet_room_chosen')
        same_area_rooms = request.POST.get('same_area_rooms')

        prope = Property.objects.filter(id=id)
        owner = (prope[0].owner)
        p_name = (prope[0].p_name).capitalize()
        p_address = (prope[0].p_address)
        p_state = (prope[0].p_state)
        p_type = (prope[0].p_type).capitalize()
        phone = (prope[0].phone)
        

        p_time_area=(prope[0].p_time_area)
        if p_time_area=="Month":
            t_price = (prope[0].p_price)/30
            p_price=(prope[0].p_price)/30
        elif p_time_area=="Day":
            t_price = (prope[0].p_price)
            p_price=(prope[0].p_price)
        elif p_time_area=="Hour":
            t_price = (prope[0].p_price)*24
            p_price=(prope[0].p_price)*24
        elif p_time_area=="Year":
            t_price = (prope[0].p_price)/365
            p_price=(prope[0].p_price)/365

        p_price = p_price * days
        final_price = p_price - (p_price * .1)
        Due_date = str(date.today())
        print(tel)
        print("------")
        print(type(phone))

        user_id = (User_Registration.objects.get(user=request.user).id)
        print(user_id)
        print(owner.id, Due_date, p_name, p_type,
              p_address, p_state, CheckIN, CheckOUT,
              firstName, lastname, tel, People, t_price,
              p_price, final_price, days)
        
        register = Booking(user_id=user_id, owner_id=owner.id, Due_date=Due_date, p_name=p_name, p_type=p_type,
                           p_address=p_address, p_state=p_state, Check_IN=CheckIN, Check_OUT=CheckOUT,
                           firstName=firstName, lastName=lastname, Phone_no=phone, People=People, p_price=t_price,
                           T_price=p_price, F_price=final_price, Days=days, tel=tel)
        print(register)
        register.save()
        param = {'Due_date': Due_date, 'p_name': p_name, 't_price': t_price, 'days': days, 'p_type': p_type,
                 'final_price': final_price, 'p_price': p_price, 'firstName': firstName, 'lastName': lastname,
                 'tel': tel, 'People': People, 'p_address': p_address, 'p_state': p_state, 'phone': phone,
                 'CheckIN': CheckIN, 'CheckOUT': CheckOUT,'pform':pform}

        print("----------------------------------------------------")

        return render(request, 'invoice.html', param)

    prope = Property.objects.filter(id=id)
    owner = (prope[0].owner)
    p_name = (prope[0].p_name)
    p_city = (prope[0].p_city)
    p_state = (prope[0].p_state)
    email = (prope[0].email)
    area_code = (prope[0].area_code)
    phone = (prope[0].phone)
    p_type = (prope[0].p_type)
    p_address = (prope[0].p_address)
    execting_cus = (prope[0].execting_cus)
    p_price = (prope[0].p_price)
    p_time_area = (prope[0].p_time_area)
    p_rooms_available = (prope[0].p_rooms_available)
    p_floor_no = (prope[0].p_floor_no)
    p_sharing_member = (prope[0].p_sharing_member)
    tenants_preffered = (prope[0].tenants_preffered)
    photo1 = (prope[0].photo)
    photo2 = (prope[0].photo1)
    photo3 = (prope[0].photo2)
    photo4 = (prope[0].photo3)
    photo5 = (prope[0].photo4)

    p_amanities = (prope[0].p_amanities).replace("'", '').strip("][").split(',')
    house_rules = (prope[0].house_rules).replace("'", '').strip("][").split(',')

    params = {'id': id, 'owner': owner, 'p_name': p_name, 'p_city': p_city, 'p_state': p_state,
              'email': email, 'area_code': area_code, 'phone': phone, 'p_type': p_type, 'p_address': p_address,
              'execting_cus': execting_cus, 'p_price': p_price, 'p_time_area': p_time_area,
              'p_rooms_available': p_rooms_available, 'p_floor_no': p_floor_no, 'p_sharing_member': p_sharing_member,
              'tenants_preffered': tenants_preffered, 'photo1': photo1, 'photo2': photo2, 'photo3': photo3,
              'photo4': photo4, 'photo5': photo5, 'p_amanities': p_amanities, 'house_rules': house_rules,'pform':pform}

    print((prope[0].p_name, params))

    return render(request, 'checkout.html', params)


def invoice(request, id):
    pform=User_Registration.objects.all()
    prope = Booking.objects.filter(id=id)
    print(prope)

    id = prope[0].id
    Due_date = prope[0].Due_date
    p_name = prope[0].p_name
    p_type = prope[0].p_type
    p_address = prope[0].p_address
    p_state = prope[0].p_state
    CheckIN = prope[0].Check_IN
    CheckOUT = prope[0].Check_OUT
    firstName = prope[0].firstName
    lastName = prope[0].lastName
    tel = prope[0].tel
    phone = prope[0].Phone_no
    People = prope[0].People
    t_price = prope[0].p_price
    p_price = prope[0].T_price
    final_price = prope[0].F_price
    days = prope[0].Days

    params = {'id': id, 'Due_date': Due_date, 'p_name': p_name, 't_price': t_price, 'days': days, 'p_type': p_type,
              'final_price': final_price, 'p_price': p_price, 'firstName': firstName, 'lastName': lastName, 'tel': tel,
              'People': People, 'p_address': p_address, 'p_state': p_state, 'phone': phone, 'CheckIN': CheckIN,
              'CheckOUT': CheckOUT,'pform':pform}
    return render(request, 'invoice.html', params)


def my_booking(request):
    pform=User_Registration.objects.all()
    user_id = (User_Registration.objects.get(user=request.user).id)
    print(user_id)
    prope = Booking.objects.filter(user_id=user_id)
    parmas = {'prope': prope,'pform':pform}

    return render(request, 'my_booking.html', parmas)


def Services(request):
    return render(request,"Services.html")

# def base(request):
#     pform=User_Registration.objects.all()
#     context={'pform':pform}
#     return render(request,"base.html",context)