from django.shortcuts import render,HttpResponse
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    return render(request,'index.html')

def Home(request):
    product = Product.objects.filter(category = "Best")
    context = {
        'product':product
    }
    return render(request,'Home.html',context)

def blog(request):
    return render(request,'blog.html')

def about(request):
    return render(request,'about.html')

def blog_details(request):
    return render(request,'blog-details.html')

def checkout(request):
    return render(request,'checkout.html')

def contact(request):
    return render(request,'contact.html')

def shop_details(request,id):
    data = Product.objects.get(id=id)
    print(data)
    context = {
        'data':data
    }
    return render(request,'shop-details.html',context)

def shop(request):
    data = Product.objects.all()
    # context = {
    #     'mydata':data
    # }
    return render(request,'shop.html',{'mydata':data})

def shopping_cart(request):
    return render(request,'shopping-cart.html')

def signup(request):
    if request.method == "POST":
        uname = request.POST['username']
        uemail = request.POST['email']
        upassword = request.POST['password']
        upassword1 = request.POST['password1']
        
        user = User(username=uname,email=uemail)
        
        if User.objects.filter(username=uname).first():
            messages.success(request,'username already taken !!!')
        elif upassword==upassword1:
          user.set_password(upassword)
          user.save()
          messages.success(request,'User account successfully create !!!')
        else:
            messages.success(request,"password field not match !!!")
        
    return render(request,'signup.html')

def loginhandle(request):
    return render(request,'login.html')


def get_data(request):
    pass



