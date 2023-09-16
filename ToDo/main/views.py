from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Review, TaskName, Inter_Task
from .forms import AddReviewForm, NewGlobalTaskForm, NewInterTaskForm


def home_window(request):
    return redirect('todo')


def todo_window(request):
    reviews = None
    form = None
    if request.user.is_authenticated:
        reviews = Review.objects.all().filter(author=request.user)
        title = 'Your ToDo'
        form = AddReviewForm(author=request.user)
        if request.method == 'POST':
            form = AddReviewForm(request.POST, author=request.user)
            if form.is_valid():
                form.save()
                return redirect('todo')
            else:
                error = form.errors
    else:
        title = 'Login or Register to access notes'
    data = {
        'title': title,
        'reviews': reviews,
        'form': form
    }
    return render(request, 'main/todo.html', data)


def change_task_status(request, id, status, type):
    if type:
        inter_task = Inter_Task.objects.get(id=id)
        inter_task.is_done = status
        inter_task.save()
        global_task = TaskName.objects.get(id = inter_task.global_task_id.id)
        if status == 'True':
            global_task.tasks_count -=1
        else:
            global_task.tasks_count +=1
        global_task.save()
        inter_task.save()
        return redirect('int_task', global_task.id)
    else:
        review = Review.objects.get(id=id)
        review.is_done = status
        review.save()
        return redirect('todo')


def delete_tasks(request, type, id):
    if type == 0:
        reviews = Review.objects.all().filter(is_done=True)
        for object in reviews:
            object.delete()
        return redirect('todo')
    elif type == 1:
        inter_task = Inter_Task.objects.get(id=id)
        error = inter_task.task_text
        global_task = TaskName.objects.get(id=inter_task.global_task_id.id)
        global_task.tasks_count -= 1
        global_task.save()

        inter_task.delete()
        return redirect('int_task', global_task.id)
    elif type == 2:
        global_task = TaskName.objects.get(id = id)
        inter_tasks = Inter_Task.objects.all().filter(global_task_id=id)
        for inter_task in inter_tasks:
            inter_task.delete()
        global_task.delete()
        return redirect('manager')




def task_manager_window(request):
    tasks = None
    if request.user.is_authenticated:
        tasks = TaskName.objects.all().filter(author=request.user)
        title = 'Current Tasks'
    else:
        title = 'Login or Register to access notes'
    data = {
        'title': title,
        'tasks': tasks,
    }
    return render(request, 'main/task_manager.html', data)


@login_required
def add_task_window(request):
    global_task_form = NewGlobalTaskForm(author=request.user)
    inter_task_form = NewInterTaskForm(global_task_id=None)
    error = ''
    if request.method == 'POST':
        if 'global_task_btn' in request.POST:
            global_task_form = NewGlobalTaskForm(request.POST, author=request.user)
            if global_task_form.is_valid():
                global_task_form.save()
                global_task_id = TaskName.objects.get(name=request.POST['name']).id
                return redirect('int_task', global_task_id)
            else:
                error = 'LOL'
        elif 'btn1' in request.POST:
            error = "Заполните, пожалуйста, наименование основной цели"

    data = {
        'error': error,
        'form1': global_task_form,
        'form2': inter_task_form,
        'flag': 'start',
    }
    return render(request, 'main/new_task.html', data)


@login_required
def inter_task_window(request, id):
    global_task = TaskName.objects.get(id=id)
    inter_task_form = NewInterTaskForm(global_task_id=None)
    error = ''
    inter_tasks = Inter_Task.objects.all().filter(global_task_id=global_task)
    count = inter_tasks.count()

    if request.method == 'POST':
        inter_task_form = NewInterTaskForm(request.POST, global_task_id=global_task)
        if inter_task_form.is_valid():
            global_task.tasks_count += 1
            inter_task_form.save()
            global_task.save()
            return redirect('int_task', id)
        else:
            error = 'LOL'

    data = {
        'form1': global_task,
        'form2': inter_task_form,
        'flag': 'inter',
        'id': id,
        'error': error,
        'inter_tasks': inter_tasks,

    }
    return render(request, 'main/new_task.html', data)


@login_required
def edit_task_window(request, id):
    global_task = TaskName.objects.get(id=id)
    global_task_form = NewGlobalTaskForm(author=request.user)
    inter_task_form = NewInterTaskForm(global_task_id=None)
    error = global_task.name
    if request.method == 'POST':
        global_task.name = request.POST['name']
        global_task.save()
        error = f"Новое имя: \"{request.POST['name']}\" сохранено!"

    data = {
        'form1': global_task_form,
        'flag': 'edit',
        'id': id,
        'error': error
    }
    return render(request, 'main/new_task.html', data)
