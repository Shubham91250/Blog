from django.shortcuts import render,HttpResponse
from .models import *
from datetime import datetime

# Create your views here.
def home(request):
    
    return render(request,'home.html')



def about(request):
    return render(request,'about.html')

def blog(request):
    popularobj=Popular_Blog.objects.all()
    context={'name':'name','popularobj':popularobj}
    return render(request,'blog.html',context)
def show_blog(request,pk):
    showBlogObj=Popular_Blog.objects.get(pk=pk)
    return render(request,'show_blog.html',{'showBlogObj':showBlogObj})
# def blog2(request):
#     regularobj=Regular_Blog.objects.all()
#     context={'name':'name','regularobj':regularobj}
#     return render(request,'blog.html',context)
def contact(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']

        if len(name)>1 and len(email)>1 and len(str(phone))==10 and len(message)>1:
            contactobj=ContactTb(name=name,email=email,phone=phone,message=message)
            contactobj.save()
    return render(request,'contact.html')