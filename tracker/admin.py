from django.contrib import admin
from .models import Goal, Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "priority", "due_date", "completed")
    list_filter = ("completed", "priority")
    search_fields = ("title", "user__username")

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "target_date", "completed")
    list_filter = ("completed",)
    search_fields = ("title", "user__username")
