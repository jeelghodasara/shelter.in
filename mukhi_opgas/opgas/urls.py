from django.urls import path
from . import views
from .views import pgindex,Base_pgindex

urlpatterns=[
    path("",views.pgindex, name="pgindex"),
    # path("Account",views.Account, name="Account"),
    path("addproperty",views.Add_property , name="addproperty"),
    path("OwnerDashbord",views.Owner_dashbord, name="Owner_dashbord"),
    path("Charts",views.Charts, name="Charts"),
    path("Forgotpassword",views.Forgot_password, name="Forgot_password"),
    path("admindashbord",views.Admin_Dashbord, name="admindashbord"),
    path("Profile",views.Profile, name="Profile"),
    path("plistpage/<str:type>",views.plistpage, name="Forgot_password"),
    path("plistpagecity/<str:city>", views.plistpagecity, name="Forgot_password"),
    path("plistpagestate/<str:state>", views.plistpagestate, name="Forgot_password"),
    path("plistpageprice/<str:price>", views.plistpageprice, name="Forgot_password"),

    path("view_page/<int:id>",views.view_page, name="view_page"),


    path("Checkout/<int:id>",views.Checkout, name="view_page"),
    path("invoice/<int:id>",views.invoice, name="view_page"),
    path("my_booking", views.my_booking, name="my_booking"),

    path("Services",views.Services, name="Services")

]