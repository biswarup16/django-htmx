from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model

# Create your views here.

def index(request):
    return render(request,'index.html')

def search(request):
    username = request.POST.get('username')
    print(username)
    mylist = ["apple", "banana", "cherry"]

    # for i in mylist:
    if username in mylist:
            # return HttpResponse('<div style="color:red">The Username is Already Exists</div>')
            context={'obj':username}
            # print(i + 'hello')
            return render(request,'search.html',context)
    else:
            return HttpResponse('<div style="color:red">The Fruit in Not Available</div>')       


    
        
