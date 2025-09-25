from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from projects.forms import CreateTaskForm, UpdateTaskForm
from projects.models import Projects, Tasks


class ProjectListView(ListView):
    model = Projects
    template_name = 'projects/table.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CreateTaskForm()
        return context


class ProjectCreateView(CreateView):
    model = Projects
    template_name = 'partials/projects/project_create_form.html'
    fields = '__all__'

    def form_valid(self, form):
        project = form.save()
        html = render_to_string('partials/projects/project_card.html', {'project': project})
        return HttpResponse(html)


class ProjectUpdateView(UpdateView):
    model = Projects
    template_name = 'partials/projects/project_update_form.html'
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save()
        html = render_to_string('partials/projects/project_card.html', {'project': self.object})
        return HttpResponse(html)


class ProjectDeleteView(DeleteView):
    model = Projects

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        # После удаления возвращаем обновлённый список проектов
        projects = Projects.objects.all()
        html = render_to_string('partials/projects/projects_list.html', {'projects': projects})
        return HttpResponse(html)


class TaskCreateView(CreateView):
    model = Tasks
    form_class = CreateTaskForm

    def form_valid(self, form):
        project = Projects.objects.get(id=self.kwargs.get('project_id'))
        form.instance.project = project
        task = form.save()

        if self.request.headers.get("HX-Request"):
            html = render_to_string("partials/tasks/list.html", {"task": task})
            return HttpResponse(html)

        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    model = Tasks
    form_class = UpdateTaskForm
    template_name = 'partials/tasks/task_update_form.html'

    def form_valid(self, form):
        task = form.save()
        if self.request.headers.get("HX-Request"):
            html = render_to_string("partials/tasks/list.html", {"task": task})
            return HttpResponse(html)
        return super().form_valid(form)
