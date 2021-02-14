from django.shortcuts import render
from django.http import HttpResponse
from .models import Property
# Create your views here.




def pgindex(request):


    pro1=Property()
    pro1.p_name="Fortune Hotel"
    pro1.p_city="Rajkot"
    pro1.p_floor="25"
    pro1.p_price="5000"
    pro1.p_bhk="3 BHK"
    pro1.p_img="Fortune.jpg"

    pro2=Property()
    pro2.p_name="VILLA"
    pro2.p_city="Rajkot"
    pro2.p_floor="3"
    pro2.p_price="1500000"
    pro2.p_bhk="5 BHK"
    pro2.p_img="Fortune.jpg"

    pro3=Property()
    pro3.p_name="PG"
    pro3.p_city="Ahamdabad"
    pro3.p_floor="10"
    pro3.p_price="6500"
    pro3.p_bhk="3 BHK"
    pro3.p_img="Fortune.jpg"

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

    props1=[pro1,pro2,pro3]
    props2=[pro4,pro5,pro6]
    props3=[pro7,pro8,pro9]


    return render(request, 'pgindex.html', {'props1':props1, 'props2':props2, 'props3':props3})


def Account(request):
         return render(request, "mysite/signup.html")

   