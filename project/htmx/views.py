from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model
from . models import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def search(request):
    username = request.POST.get('username')
    print(username)
    mylist = ["apple", "banana", "cherry"]

    if len(username) >0:


        student_obj = Student.objects.filter(name__icontains=username)[:3]

        return render(request,'search.html',{'student_obj':student_obj})
    else:
        return render(request,'search.html',{'student_obj':None})


    # # for i in mylist:
    # if username in mylist:
    #         # return HttpResponse('<div style="color:red">The Username is Already Exists</div>')
    #         context={'obj':username}
    #         # print(i + 'hello')
    #         return render(request,'search.html',context)
    # else:
    #         return HttpResponse('<div style="color:red">The Fruit in Not Available</div>')       


    
        
