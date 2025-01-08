from django.shortcuts import render
from .form import DataForm
from . import models
#return home.html

def home(request):
    anouncement=models.Announcements.objects.all().order_by('-id')[:4]
    programs=models.Programs.objects.all().order_by('-program_name')[:10]
    best=models.Herroes.objects.all().order_by('-id')[:1]
    return render(request,'home.html',{'announcements':anouncement,'programs':programs,'best':best})

def herroes(request):
    best=models.Herroes.objects.all().order_by('-id')
    return render(request,'herroes.html',{'best':best})

def about(request):
    return render(request,'about.html')

def anouncements(request):
    anouncement=models.Announcements.objects.all().order_by('-id')
    return render(request,'anouncements.html',{'announcements':anouncement})

def courses(request):
    programs=models.Programs.objects.all().order_by('-program_name')
    return render(request,'courses.html',{'programs':programs})

def application(request):
    if request.method=="POST":
     form=DataForm(request.POST or None,request.FILES)
     #incase form is validated
     if form.is_valid():
        form.save()
        messages.success(request,"you have successfully registered.")
        #clear the form
        form=DataForm()
        return render(request,"application.html",{'form':form})
     else:
        return render(request,"application.html",{'form':form})
    else:
        form=DataForm()
        return render(request,"application.html",{'form':form})
def status(request):
    return render(request,'status.html')

