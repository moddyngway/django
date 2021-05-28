from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    context = {
        "title": "moddyngway's site",
        "tasks": tasks
    }
    return render(request, "main/index.html", context)


def about(request):
    return render(request, "main/about.html")


def create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    form = TaskForm()
    context = {
        "form" : form
    }
    return render(request, "main/create.html", context)


def fumo(request):
    return render(request, "main/fumo.html")
