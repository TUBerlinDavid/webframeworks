from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from todo.models import Todo
from todo.forms import TaskForm

# Create your views here.
def index(request):
    todo_list = Todo.objects.order_by('id')
    return render(request, 'index.html', { 'todo_list': todo_list })


def add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            update_or_create_task(form, None)
            messages.success(request, 'ToDo successful created!')
            return redirect('index')
    else:
        form = TaskForm()
    return render(request, 'add.html', { 'form': form })


def edit(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            update_or_create_task(form, todo_id)
            messages.success(request, 'ToDo #%s successful updated!' % todo_id)
            return redirect('index')
    else:
        form = TaskForm(initial={ 'task': todo.task, 'progress': todo.progress, 'deadline_date': todo.deadline_date })
    return render(request, 'edit.html', { 'todo': todo, 'form': form })


def delete(request, todo_id):
    get_object_or_404(Todo, id=todo_id).delete()
    messages.success(request, 'ToDo #%s successful deleted!' % todo_id)
    return redirect('index')


def imprint(request):
    return render(request, 'imprint.html')


def update_or_create_task(form, todo_id):
    return Todo.objects.update_or_create(id=todo_id, defaults={
        'task': form.cleaned_data.get('task'),
        'progress': form.cleaned_data.get('progress'),
        'deadline_date': form.cleaned_data.get('deadline_date')
    })