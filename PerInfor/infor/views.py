from django.shortcuts import render,redirect
from .models import Infor
# Create your views here.

def index(requset):

    infos = Infor.objects.all()
    return render(requset,'index.html',{"infos":infos})

def add(request):

    if request.method =='GET':
        return render(request,'add_form.html')
    elif request.method=='POST':
        name = request.POST.get('name','')
        job = request.POST.get('job','')
        classmate = request.POST.get('classmate','')
        home = request.POST.get('home','')
        school = request.POST.get('school', '')
        life_info = request.POST.get('life_info','')
        job_info = request.POST.get('job_info','')
        classmate_info = request.POST.get('classmate_info','')
        home_info = request.POST.get('home_info','')
        school_info = request.POST.get('school_info','')
        res = Infor(name=name,job=job,classmate=classmate,home=home,school=school,life_info=life_info,job_info=job_info,classmate_info=classmate_info,home_info=home_info,school_info=school_info)
        res.save()
        return redirect('/')

def delete(requset):

        id = requset.GET.get('id')
        id = int(id)
        if id:
            Infor.objects.get(id=id).delete()
            return redirect('/')

def update(requset):
    if requset.method=='GET':
        id = requset.GET.get('id')
        id = int(id)

        infos = Infor.objects.get(id = id)
        return render(requset,'up_form.html',{"infos":infos})
    elif requset.method == 'POST':
        id = requset.POST.get('id')
        id = int(id)
        info = Infor.objects.get(id=id)
        info.name = requset.POST.get('name', '')
        info.job = requset.POST.get('job', '')
        info.classmate = requset.POST.get('classmate', '')
        info.home = requset.POST.get('home', '')
        info.school = requset.POST.get('school', '')
        info.life_info = requset.POST.get('life_info', '')
        info.job_info = requset.POST.get('job_info', '')
        info.classmate_info = requset.POST.get('classmate_info', '')
        info.home_info = requset.POST.get('home_info', '')
        info.school_info = requset.POST.get('school_ info', '')
        info.save()
        return redirect('/')


def chak(request):
    if request.method=='GET':
        id = request.GET.get('id')
        id = int(id)
        infos = Infor.objects.get(id=id)
        return render(request,'2.html',{"infos":infos})