from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import User_Registration
from .forms import RegisterForm
# Create your views here.


def login(request):
    if request.method == "POST":
        # email=request.POST.get('Email')
        # get_user_name_email=User.objects.get(email=email)
        user = auth.authenticate(username=request.POST.get('Username'), password=request.POST.get('Password'))
        if user is not None:
            auth.login(request,user)
            showusername=request.POST["Username"]
            return render(request,"pgindex.html",{'showusername':showusername})
        else:
            return render(request,'mysite/signup.html',{'error':"Invalid login candidates."})
    else:
        render(request,'mysite/signup.html')



def logout(request):
    auth.logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")

def Register(request):
    if request.method == 'POST':
        username=request.POST['Username']
        try:
            user=User.objects.get(username=username)
            return render(request, "mysite/signup.html",{'error':"Username has already been taken"})
        except User.DoesNotExist:
            user=User.objects.create_user(username=request.POST.get('Username'),password=request.POST.get('Password'),email=request.POST.get('Email'))
            user_type=request.POST.get('u_selection')
            mobile_no=request.POST.get('Mobile_no')
            data=User_Registration(user_type=user_type,mobile_no=mobile_no,user=user)
            data.save()
            auth.login(request,user)
            return HttpResponse("SIGGNED UP!!!")
    else:
        return render(request,"mysite/signup.html")

