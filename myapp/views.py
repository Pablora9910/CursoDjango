from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Project,Task
from django.shortcuts import get_object_or_404, render,redirect
from .formulario import *

# Create your views here.
def hello(request,username):  # sourcery skip: replace-interpolation-with-fstring
    # print(username)
    return render("<h1>Hello %s</h1>" % username)
def about(request,username):
     return render(request,'about.html',{
        'username' : username
    })
def index(request):
    title = 'Que Onda'
    return render(request,'index.html',{
        'title' : title
    })
def project(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    
    return render(request,'Project.html',{
        'projects' : projects
    })
def task(request):
     # tasks = get_object_or_404(Task, id = idTask)
    tasks = Task.objects.all()
    return render(request,'Task.html',{
        'tasks' : tasks
    })
    
def create_task(request):  # sourcery skip: remove-unnecessary-else
    if request.method == 'GET':
       return render(request,'create_task.html',{
            'form': CreateNewTask() 
        })
    else:
        Task.objects.create(title = request.POST['title'],
                    description = request.POST['description'],project_id =2)
        return redirect('/task')
    
def create_project(request):  # sourcery skip: remove-unnecessary-else
    if request.method == 'GET':
       return render(request,'create_project.html',{
            'form': CreateNewProject() 
        })
    else:
        Project.objects.create(name = request.POST['name'])
        return redirect('/project/')
def task_done(request,idTask):
    task = Task.objects.get(id=idTask)
    task.done = True
    task.save()
    return redirect('/task')
def task_delte(request,idTask):
    task = Task.objects.get(id=idTask)
    task.delete()
   # task.save()
    return redirect('/task')


