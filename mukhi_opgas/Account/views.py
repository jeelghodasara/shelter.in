from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect 
from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import User_Registration
from .forms import RegisterForm, ProfileRegisterForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
# Create your views here.


def login(request):
    if request.method=="POST":
        username=request.POST.get('Username')
        password=request.POST.get('Password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
    else:
        return render(request, "mysite/signup.html")
    

@login_required
def logout(request):
    auth.logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")

def Register(request):
    if request.method == 'POST':    

        profileform=ProfileRegisterForm(data=request.POST)
        form=RegisterForm(data=request.POST)
        if form.is_valid():
            user=form.save()
            user.password=make_password(user.password)
            user.save()
            auth.login(request,user)
            user_type=request.POST.get('u_selection')
            if user_type=="Owner":
                data=User_Registration(user_type=request.POST.get('u_selection'),mobile_no=request.POST.get('mobile_no'),user=user)
                data.save()
            
        return redirect('/')

        context={"form":profileform,'mainform':form}
        return render(request,"mysite/signup.html",context)
    else:
        form=ProfileRegisterForm()
        mainform=RegisterForm()
        context={"form":form,'mainform':mainform}
        return render(request,"mysite/signup.html",context)

