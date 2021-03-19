from django.urls import path
from . import views
# from Account.views import signin,login,Register

urlpatterns=[
    path("Register",views.Register, name="Register"),
    path("login",views.login, name="login")
]