from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from registration.models import Mentor, Course
# Create your views here.
def index(request):
    return render(request,"index.html")

def course(request):
    
    if request.method == 'POST':
        c_code = request.POST['code']
        c_desc = request.POST['description']
        data=Course(code=c_code, description=c_desc)
        data.save()
        
        mycourse = Course.objects.all().values()
        context = {
            'message': 'Data Saved',
            'data' : mycourse,
        }

    else:
        mycourse = Course.objects.all().values()
        context = {
            'message': ' ',
            'data' : mycourse,
        }

    return render (request,"course.html",context)

def update_course(request,code):
    data=Course.objects.get(code=code)
    dict = {
        'data':data
    }
    return render (request, "update_course.html",dict)

def save_update_course(request,code):
    c_desc=request.POST['description']
    data=Course.objects.get(code=code)
    data.description=c_desc
    data.save()
    return HttpResponseRedirect(reverse("course"))

def delete_course(request,code):
    data = Course.objects.get(code=code)
    data.delete()
    return HttpResponseRedirect(reverse('course'))
