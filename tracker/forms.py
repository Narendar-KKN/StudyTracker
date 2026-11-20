from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task, Goal

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class TaskForm(forms.ModelForm):
    due_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date"})
    )

    class Meta:
        model = Task
        fields = ("title", "description", "due_date", "priority")
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4, "placeholder": "What do you need to study?"}),
        }

class GoalForm(forms.ModelForm):
    target_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date"})
    )

    class Meta:
        model = Goal
        fields = ("title", "target_date")
