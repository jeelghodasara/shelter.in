from django.urls import path
from . import views
from .views import pgindex,Base_pgindex

urlpatterns=[
    path("",views.pgindex, name="pgindex"),
    # path("Account",views.Account, name="Account"),
    path("addproperty",views.Add_property , name="addproperty"),
    path("OwnerDashbord",views.Owner_dashbord, name="Owner_dashbord"),
    path("Charts",views.Charts, name="Charts"),
    path("Forgotpassword",views.Forgot_password, name="Forgot_password")
]