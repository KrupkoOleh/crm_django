from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic import ListView, CreateView

from projects.models import Projects


class ProjectListView(ListView):
    model = Projects
    template_name = 'projects/table.html'
    context_object_name = 'projects'


class ProjectCreateView(CreateView):
    model = Projects
    template_name = 'partials/projects/project_create_form.html'
    fields = '__all__'

    def form_valid(self, form):
        project = form.save()
        html = render_to_string('partials/projects/project_card.html', {'project': project})
        return HttpResponse(html)

