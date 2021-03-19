from django.urls import path
from . import views
from .views import pgindex,Base_pgindex

urlpatterns=[
    path("",views.pgindex, name="pgindex"),
    # path("Account",views.Account, name="Account"),
    path("addproperty",views.Add_property , name="addproperty"),
]