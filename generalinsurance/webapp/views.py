from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.
@login_required
def loginview(request):
    if request.method=='GET':
        return render(request,'login.html',{})
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)

            return render(request,'mainmenu.html',{})
        else:
            return render(request,'login.html',{})

def logout_view(request):
    logout(request)
    return render(request,'logout.html',{})

def homepage(request):
    return render(request,'Home.html',{})

def about_views(request):
    return render(request,'About.html')
def sign_view(request):
    return render(request,'signup.html')
def mainpage_view(request):
    return render(request,'mainmenu.html')




