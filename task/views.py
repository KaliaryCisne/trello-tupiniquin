from django.shortcuts import render, redirect
from task.models import Status, Description


def home(request):
    name = "Kaliary"
    tasks = Description.objects.all()
    status = Status.objects.all()
    context = {
        'name': name,
        'tasks': tasks,
        'status': status,
    }
    return render(request, 'task/home.html', context)

# Renderiza a view para criar uma nova task
def createTask(request):
    status = Status.objects.all()
    context = {
        'status': status,
    }
    return render(request, 'task/description/create.html', context)

# Renderiza a view para editar uma task
def editTask(request, id):
    task = Description.objects.get(id=id)
    status = Status.objects.all()
    context = {
        'task': task,
        'status': status,
    }
    return render(request, 'task/description/update.html', context)

# Deleta umas task
def destroyTask(request, id):
    task = Description.objects.get(id=id)
    task.delete()
    return redirect("/")

# Exibe todos os status
def listStatus(request):
    status = Status.objects.all()
    context = {
        'status': status,
    }
    return render(request, 'task/status/list.html', context)

# Persiste no banco uma tarefa
def persistenceTask(request):

    name = request.POST["name"]
    content = request.POST["description"]
    status_id = request.POST["status-id"]
    status = Status.objects.get(id=status_id)

    if "task-id" in request.POST:
        task_id = request.POST["task-id"]
        task = Description.objects.get(id=task_id)
        task.name = name
        task.content = content
        task.status = status
        task.save()
    else:
        Description.objects.create(name=name, content=content, status=status)

    return redirect("/")

# Renderiza a view para criar um novo status
def createStatus(request):
    return render(request, 'task/status/create.html')

# Persiste no banco um novo status
def persistenceStatus(request):
    name = request.POST["name"]
    Status.objects.create(name=name)
    return redirect("status-list")

# Apaga um status
def destroyStatus(request, id):
    status = Status.objects.get(id=id)
    status.delete()
    return redirect("status-list")
