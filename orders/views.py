from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import FoodItem

def Index(request):
    items=FoodItem.objects.all()
    context ={
    'items':items
    }
    return render(request,'ind.html',context)


def home(request):
    return render(request, 'base.html')

def menu(request):
    menu_items = FoodItem.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def detail(request):
    return render(request,'detail.html')


def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('Index')
    return render(request, 'log.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return render(request, 'regi.html', {'error': 'Username already exists'})
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request,user)
            # Redirect to a success page.
            return redirect('success')
    else:
        return render(request,'regi.html')



def logout_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('success')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')











