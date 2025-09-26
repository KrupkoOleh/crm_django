from django.contrib import admin

from projects.models import Projects, Tasks


class TasksAttributeInline(admin.TabularInline):
    model = Tasks
    extra = 1


@admin.register(Projects)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [TasksAttributeInline]
