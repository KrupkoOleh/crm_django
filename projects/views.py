from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from projects.forms import CreateTaskForm, UpdateTaskForm
from projects.models import Projects, Tasks


class ProjectListView(ListView):
    model = Projects
    template_name = 'projects/table.html'
    context_object_name = 'projects'
    login_url = reverse_lazy('account_login')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = Projects.objects.filter(owner=self.request.user)
        qs = qs.prefetch_related('tasks')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CreateTaskForm()
        return context


class ProjectCreateView(CreateView):
    model = Projects
    template_name = 'partials/projects/project_create_form.html'
    fields = ['name']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        task_create_form = CreateTaskForm()
        project = form.save()
        html = render_to_string('partials/projects/project_card.html', {'project': project, 'form': task_create_form})
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
        project_id = kwargs.get('pk')
        Projects.objects.filter(pk=project_id).delete()
        projects = Projects.objects.filter(owner=request.user).prefetch_related('tasks')
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


class TaskDeleteView(DeleteView):
    model = Tasks

    def post(self, request, *args, **kwargs):
        task = Tasks.objects.select_related('project').get(pk=kwargs['pk'])
        project = task.project
        task.delete()
        tasks = project.tasks.select_related('project')
        html = render_to_string('partials/tasks/tasks_list.html', {'tasks': tasks})
        return HttpResponse(html)


class TaskReorderView(View):
    def post(self, request, project_id):
        task_ids = request.POST.getlist('task')
        tasks = Tasks.objects.filter(id__in=task_ids, project_id=project_id)
        task_map = {task_id: index for index, task_id in enumerate(task_ids)}
        for task in tasks:
            task.priority = task_map[str(task.id)]
        Tasks.objects.bulk_update(tasks, ['priority'])
        return HttpResponse(status=204)
