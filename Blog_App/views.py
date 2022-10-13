
from django.shortcuts import redirect, render
from.models import Blogging
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import addblog
from django.contrib.auth.decorators import login_required

# Create your views here.
def Home(request):
    data=Blogging.objects.all()
    return render (request,"base.html",{"abc":data})

def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST["password1"]
        password2=request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exist !')
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exist !')
                return redirect("register")
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save()
                messages.info(request,"register successfully")
                return redirect("login")

        else:
            messages.info(request,"password not match correctly")
            return redirect("register")
    else:
        return render(request,"register.html")

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'username / password incorrect ! ')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    messages.info(request,"Logout successfully")
    return redirect('login')

@login_required(login_url='login')
def add_blog(request):
    if request.method == 'GET':
        form = addblog()
        return render (request,'addblog.html',{'form':form})

    else:
        form = addblog(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('Home')

def update(request,id):
    data=Blogging.objects.get(id=id)
    if request.method == 'GET':
        form = addblog(instance=data)
        return render (request,'addblog.html',{'form':form})

    else:
        form = addblog(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
        return redirect('Home')
