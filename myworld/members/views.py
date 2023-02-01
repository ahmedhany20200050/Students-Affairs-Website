# from multiprocessing import context
# from unicodedata import name
# from pydoc import render_doc
# from re import template
# from unicodedata import name
# from logging import _Level
# from multiprocessing import context
import json
from multiprocessing import context
from pickle import TRUE
from secrets import choice
from unicodedata import name
# from pydoc import render_doc
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.template import loader
# from django.urls import reverse
from .models import Employees, Students
from django.shortcuts import render,redirect
from django.urls import reverse






## the following functions are meant to load html pages only
def startPage(request):
    template = loader.get_template('start-page.html')
    return HttpResponse(template.render())


def login(request):
    # template = loader.get_template('Files/login_screen.html')
    context={
        'ok':True,
    }
    return render(request,'Files/login_screen.html',context)

def homepage(request):
    template=loader.get_template('Files/Home.html')
    return HttpResponse(template.render())

def active_inactive(request):
    # template=loader.get_template('')
    st=Students.objects.all()
    context={
        'ss':st,
    }
    return render(request,'Files/active-inactive.html',context)

def search(request):
    template=loader.get_template('Files/search.html')
    return HttpResponse(template.render())

def addStudentPage(request):
    template=loader.get_template('Files/add_student.html')
    return HttpResponse(template.render())

def editPage(request):
    template=loader.get_template('Files/edit.html')
    return HttpResponse(template.render())

def department_assignment(request):
    template=loader.get_template('Files/department_assignment.html')
    context={
        'students': request.POST.get('students'),
    }
    return HttpResponse(context,template.render())

## end of "html loading" functions

def validate(request):
    
    allStudents=Employees.objects.all().values()
    for a in allStudents:
        if a['mail']==request.POST['email']:
            if a['password']==request.POST['password']:
                template=loader.get_template('Files/Home.html')
                return HttpResponse(template.render())
    context={
        'ok':False,
    }
    return render(request,'Files/login_screen.html',context)
    # x=Employees.objects.get(mail=request.POST['email'])
    
    # if x:
    #     return HttpResponse(template)
    # else:
    #     return HttpResponse(template)





def addStudent(request):
#   x = request.POST['first']
#   y = request.POST['last']
    x=Students.objects.filter(ID=request.POST['id'])
    if x:
        context={
            'ok':False,
        }
        # template=loader.get_template('Files/add_student.html')
        return render(request,'Files/add_student.html',context)

    member = Students(
    name=request.POST['name'],
    ID=request.POST['id'],
    birth=request.POST['date'],
    gpa=request.POST['gpa'],
    male=request.POST['gender'],
    level=request.POST['level'],
    active=request.POST['status'],
    dep=request.POST['department'],
    mail=request.POST['email'],
    phone=request.POST['phone'],
    
    )
    member.save()
    return redirect(reverse("active-inactive"))

def getStudents(request):
    allStudents=Students.objects.all()
    dict={
        'first':allStudents,
    }
    return HttpResponse(dict)

def delete(request):
    x=Students.objects.get(id=request.GET['ID'])
    if x:
        Students.objects.delete(id=request.GET['ID'])
        return HttpResponse('ok')
    else:
        return HttpResponse('not ok')


def updateStudents(request):
#   first = request.POST['first']
#   last = request.POST['last']
#   s = Students.objects.get(id = request.POST['ID'])
    if 'delete' in request.POST:
        x=Students.objects.filter(ID=request.POST['id'])
        if x:
            x.delete()
            return redirect(reverse("active-inactive"))
        else:
            context={
                'ok':False,
            }
            return render(request,"Files/edit.html",context)
    
    if 'update' in request.POST:
        x=Students.objects.filter(ID=request.POST['id'])
        if x:
            a=Students.objects.get(ID=request.POST['id'])
            k=a.dep
            a.delete()
            member = Students(
            name=request.POST['name'],
            ID=request.POST['id'],
            birth=request.POST['date'],
            gpa=request.POST['gpa'],
            male=request.POST['gender'],
            level=request.POST['level'],
            active=request.POST['status'],
            dep=k,
            mail=request.POST['email'],
            phone=request.POST['phone'],
            )
            member.save()
            return redirect(reverse("active-inactive"))
        else:
            context={
                'ok':False,
            }
            # return HttpResponseRedirect(reverse('active-inactive'))
            return render(request,"Files/edit.html",context)

    
def changeStatus(request,id):
    x=Students.objects.get(ID=id)
    if x.active:
        x.active=False
    else:
        x.active=True
    x.save()

    return HttpResponseRedirect(reverse('active-inactive'))

def change_status(request,pk):
    print("Hello")
    student=Students.objects.get(ID=pk)
    print(student.ID)
    if(student.active==True):
            student.active=False
    else:
            student.active=True
    student.save()
    return HttpResponse("The student's status has changed successfully reload the page to see the changes")
    
def assign(request,id):
    choice=request.POST['dep']
    # id=request.POST['idd']
    x=Students.objects.get(ID=id)
    if x.level == 1:
        context={
                'num':5
            }
        return render(request,"Files/search.html",context)

    if x.level == 2:
        context={
                'num':5
            }
        return render(request,"Files/search.html",context)
    if x.level == 4:
        context={
                'num':5
            }
        return render(request,"Files/search.html",context)

    x.dep=choice
    x.save()
    context={
        'num':1
    }
    return render(request,"Files/search.html",context)
    

def getSt(request):
    choice=request.POST['select']
    if choice== 'id':
        x=Students.objects.filter(ID=request.POST['search'],active = True)
        # x.filter()
        context={
            'students':x
        }
        if x:
            return render(request,'Files/department_assignment.html',context)
        else:
            context={
                'num':2
            }
            return render(request,"Files/search.html",context)        
    else:
        x=Students.objects.filter(name=request.POST['search'],active = True)
        # x.filter(active = True)
        context={
            'students':x
        }
        if x:
            return render(request,'Files/department_assignment.html',context)
        else:
            context={
                'num':2
            }
            return render(request,"Files/search.html",context)

    





# def index(request):
#   mymembers = Members.objects.all().values()
#   template = loader.get_template('index.html')
#   context = {
#     'mymembers': mymembers,
#   }
#   return HttpResponse(template.render(context, request))

# def start(request):
#   mymembers = Students.objects.all().values()
#   template = loader.get_template('start-page.html')
#   context = {
#     'mymembers': mymembers,
#   }
#   return HttpResponse(template.render(context, request))


# def add(request):
#   template = loader.get_template('add.html')
#   return HttpResponse(template.render({}, request))

# def addrecord(request):
#   x = request.POST['first']
#   y = request.POST['last']
#   member = Members(firstname=x, lastname=y)
#   member.save()
#   return HttpResponseRedirect(reverse('index'))

# def delete(request, id):
#   member = Members.objects.get(id=id)
#   member.delete()
#   return HttpResponseRedirect(reverse('index'))

# def update(request, id):
#   mymember = Members.objects.get(id=id)
#   template = loader.get_template('update.html')
#   context = {
#     'mymember': mymember,
#   }
#   return HttpResponse(template.render(context, request))

# def updaterecord(request, id):
#   first = request.POST['first']
#   last = request.POST['last']
#   member = Members.objects.get(id=id)
#   member.firstname = first
#   member.lastname = last
#   member.save()
#   return HttpResponseRedirect(reverse('index'))
