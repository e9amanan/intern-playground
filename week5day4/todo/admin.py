from django.contrib import admin

from .models import Project, Task


# Custom Action to mark tasks complete
@admin.action(description="Mark selected tasks as completed")
def make_completed(modeladmin, request, queryset):
    queryset.update(is_completed=True)


# Inline config so you can edit Tasks inside the Project screen
class TaskInline(admin.TabularInline):
    model = Task
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [TaskInline]


# Customizing the Task admin view
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "start_date", "due_date", "is_completed")
    list_filter = ("is_completed", "project")
    search_fields = ("title", "description")
    ordering = ("-due_date",)
    date_hierarchy = "due_date"
    actions = [make_completed]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
