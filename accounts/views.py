from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import views as views_auth
from django.contrib.auth import get_user_model



# Create your views here.

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
      
        
        if user is not None:
            auth.login(request, user)
            if request.user.is_authenticated and request.user.is_superuser:
                return render(request, 'admin_dashboard')
          
            return redirect("dashboard")
            
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else :
        return render(request,'login.html')

def admin_login(request):
    return render(request,'admin_login.html')



def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2: 
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('showusers')
        else:
            messages.info(request,'password is not matching')
            return redirect('register')
        return redirect('/')
        
    else :
        return render(request,'register.html')

def Finalarea(request):
    return render(request,'Finalarea.html')
def table(request):
    return render(request,'table.html') 
def doctors(request):
    return render(request,'doctors.html')
def dashboard(request):
    return render(request,'dashboard.html')  
def admin_dashboard(request):
    return render(request,'admin_dashboard.html') 

def showusers(request):
 
    User = get_user_model()
    context = User.objects.values()
    
    return render(request,'showusers.html',{'context':context})





