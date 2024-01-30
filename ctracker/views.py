from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import *
from django.contrib.auth.models import User,auth
# Create your views here.
def index(request):
  if request.method=="POST":
    food_consumed=request.POST['food_consumed']
    food=Food.objects.get(name=food_consumed)#food object
    user=request.user#current user who is logged in
    consume=Consume(user=user,food_consumed=food)
    consume.save()
    foods=Food.objects.all()
    cons_food=Consume.objects.filter(user=request.user)
  else:
    cons_food=Consume.objects.filter(user=request.user)
    foods=Food.objects.all()
  return render(request,'ctracker/index.html',{'foods':foods,'cons_food':cons_food})

def delete_consume(request,id):
  consumed_food=Consume.objects.get(id=id)
  if(request.method=='POST'):
    consumed_food.delete()
    return redirect('/')
  return render(request,'ctracker/delete.html')


def login(request):
  if request.method=='POST':
     username=request.POST['username']
     password=request.POST['password']
     
     user=auth.authenticate(username=username,password=password)
     if user is not None:
       auth.login(request,user)
       print("user verified",user.username)
       return redirect('/home')
     else:
       print("unuauthor")
       return render(request,'ctracker/login.html')  

  else:
    return render(request,'ctracker/login.html')  
  
def logout(request):
  auth.logout(request)
  print("logged out")
  return redirect('/login')

def signup(request):
  if(request.method=="POST"):
    first_name=request.POST['firstName']
    last_name=request.POST['lastName']
    username=request.POST['username']
    password1=request.POST['password1']
    password2=request.POST['password2']
    user=User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name)
    user.save()
    print("User saved")
    return redirect('/login')
  else:
    return render(request,'ctracker/signup.html')  
  
def main_page(request):
    user = request.user
    if(user.is_authenticated):
      return redirect('/home')
    else:
      return render(request,'ctracker/main.html')
