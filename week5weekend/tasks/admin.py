from django.contrib import admin
from .models import Task, Category, Tag

# Custom Action
@admin.action(description="Mark selected tasks as Done")
def mark_as_done(modeladmin, request, queryset):
    queryset.update(status='DONE')

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'due_date', 'created_at', 'category')
    list_filter = ('status', 'priority', 'created_at')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    actions = [mark_as_done]
    filter_horizontal = ('tags',) # Makes ManyToMany selection much nicer

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Task, TaskAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)