from django.shortcuts import render
from .models import Task

# def task_list(request):
#    tasks = Task.objects.all()
#    return render(request, "tasks/task_list.html", {"tasks": tasks})

class TaskListView(ListView):
    model = Task
    tamplate_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

