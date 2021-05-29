from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'pmanagement/home.html',{})

def commoninfo(request):
    return render(request,'pmanagement/commoninfo.html',{})

def user_list(request):
    pt =Users.objects.all()
    return render(request,'pmanagement/user_list.html',{'plist':pt})

def fetch(request):
    temp_username = ""
    temp_dob = ""
    temp_id = ""
    flag = 0
    if request.method == 'POST':
        temp = request.POST["UniqueID"]
        # print(temp)


        user_temp = Users.objects.order_by('FullName')
        for item in user_temp:
            if item.UniqueID == temp:
                flag = 1
                temp_username = str(item.UserName)
                temp_dob = str(item.DOB)
                temp_id = str(item.UniqueID)
                break
            else:
                flag = 999

    return render(request,'pmanagement/fetch.html',{'username':temp_username,'dob':temp_dob,'id':temp_id,'flag':flag})

def add(request):
    flag = 0
    if request.method == 'POST':
        flag = 1
        id = request.POST['UniqueID']
        uname = request.POST['UserName']
        name = request.POST['FullName']
        email = request.POST['Email']
        dob = request.POST['DOB']
        password = request.POST['Password']
        repeatpassword = request.POST['repeatpassword']

        Users.objects.create(UniqueID=id,UserName=uname,FullName=name,Email=email,DOB=dob,Password=password)
        messages.success(request, f'Patient Registered successfully')
        return render(request, 'pmanagement/home.html',{'flag':flag})
    else:
        flag = 999
        return render(request, 'pmanagement/add.html',{'flag':flag})