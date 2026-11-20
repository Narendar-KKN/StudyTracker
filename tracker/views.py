from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import GoalForm, RegisterForm, TaskForm
from .models import Goal, Task


def home(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    return render(request, "tracker/home.html")


def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Your account has been created. Welcome to StudyTracker!")
            return redirect("dashboard")
    else:
        form = RegisterForm()
    return render(request, "tracker/register.html", {"form": form})


@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    goals = Goal.objects.filter(user=request.user)
    total = tasks.count()
    completed = tasks.filter(completed=True).count()
    percentage = round((completed / total) * 100) if total else 0
    context = {
        "tasks": tasks[:6],
        "goals": goals[:4],
        "total_tasks": total,
        "completed_tasks": completed,
        "pending_tasks": total - completed,
        "percentage": percentage,
    }
    return render(request, "tracker/dashboard.html", context)


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, "tracker/task_list.html", {"tasks": tasks})


@login_required
def task_create(request):
    form = TaskForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        messages.success(request, "Study task added.")
        return redirect("task_list")
    return render(request, "tracker/task_form.html", {"form": form, "page_title": "Add a study task"})


@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    form = TaskForm(request.POST or None, instance=task)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Task updated.")
        return redirect("task_list")
    return render(request, "tracker/task_form.html", {"form": form, "page_title": "Edit study task"})


@login_required
@require_POST
def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = not task.completed
    task.save(update_fields=["completed"])
    return redirect(request.POST.get("next") or "task_list")


@login_required
@require_POST
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    messages.success(request, "Task deleted.")
    return redirect("task_list")


@login_required
def goal_list(request):
    goals = Goal.objects.filter(user=request.user)
    return render(request, "tracker/goal_list.html", {"goals": goals})


@login_required
def goal_create(request):
    form = GoalForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        goal = form.save(commit=False)
        goal.user = request.user
        goal.save()
        messages.success(request, "Study goal added.")
        return redirect("goal_list")
    return render(request, "tracker/task_form.html", {"form": form, "page_title": "Add a study goal"})


@login_required
@require_POST
def goal_toggle(request, pk):
    goal = get_object_or_404(Goal, pk=pk, user=request.user)
    goal.completed = not goal.completed
    goal.save(update_fields=["completed"])
    return redirect("goal_list")


@login_required
@require_POST
def goal_delete(request, pk):
    goal = get_object_or_404(Goal, pk=pk, user=request.user)
    goal.delete()
    messages.success(request, "Goal deleted.")
    return redirect("goal_list")
