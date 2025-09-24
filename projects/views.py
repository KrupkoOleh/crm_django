from django.views.generic import ListView

from projects.models import Projects


class ProjectListView(ListView):
    model = Projects
    template_name = 'projects/table.html'
    context_object_name = 'projects'
