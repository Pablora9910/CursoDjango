from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/<str:username>', views.about),
    path('hello/<str:username>', views.hello),
    path('project/', views.project),
    path('task', views.task),
    path('create_task/', views.create_task),
    path('create_project/', views.create_project),
    path('task_done/<int:idTask>', views.task_done, name= "task_done"),
    path('task_delete/<int:idTask>', views.task_delte, name= "task_delete"),
    
    
]