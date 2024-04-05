from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import task,members
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return HttpResponse("Go To Next Page To Add Your Task")

@login_required(login_url='signinpage')
def addtask(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        date=request.POST.get('date')
        time=request.POST.get('time')
        task.objects.create(
            name=name,
            date=date,
            time=time,
            uid_id = request.user.id
        )
       
        messages.add_message(request,messages.SUCCESS,"Succesfully added items....")
        

    return render(request,'addtask.html')    

@login_required(login_url='signinpage')
def viewtask(request):
    tasks=task.objects.filter(uid_id=request.user.id)
    return render(request,'viewtasks.html',{'tasks':tasks})




def deletetask(request,id):
    task.objects.get(id=id).delete()
    return redirect('viewpage')



def deletealltask(request):
    tas=task.objects.all()
    tas.delete()
    return redirect('addtaskpage')

@login_required(login_url='signinpage')
def edittask(request,id):
    
    item=task.objects.get(id=id)
    if item.uid_id!=request.user.id:
        return redirect('viewpage')
    if request.method == 'POST':
        name=request.POST.get('name')
        date=request.POST.get('date')
        time=request.POST.get('time')
        item.name=name
        item.date=date
        item.time=time
        item.save()
        messages.add_message(request,messages.SUCCESS,"Succesfully added items....")
        return redirect('viewpage')

    return render(request,'edittask.html',{'items':item})


def signup(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')

        usercheck=User.objects.filter(username=username)
        if len(usercheck)>0:
            return redirect('signupPage')
        
        
        if password == confirmpassword:
            user=User.objects.create_user(
                username=username,
                password=password)
            
            members.objects.create(
                name=name,
                mobile=mobile,
                email=email,
                gender=gender,
                dob=dob,
                uid_id=user.id
            )
            return redirect('signinpage')
        
    return render(request,'signup.html')


def signin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        information=authenticate(username=username,password=password)
        if information is not None:
            login(request,information)
            return redirect('addtaskpage')
    return render(request,'signin.html')

def signout(request):
    logout(request)
    return redirect('signinpage')