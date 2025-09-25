from django.urls import path

from projects.views import ProjectListView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView, TaskCreateView, \
    TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', ProjectListView.as_view(), name='projects-list'),
    path('add/', ProjectCreateView.as_view(), name='projects-create'),
    path('update/<uuid:pk>/', ProjectUpdateView.as_view(), name='projects-update'),
    path('delete/<uuid:pk>/', ProjectDeleteView.as_view(), name='projects-delete'),
    path('task/create/<uuid:project_id>/', TaskCreateView.as_view(), name='task-create'),
    path('task/update/<uuid:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('task/delete/<uuid:pk>/', TaskDeleteView.as_view(), name='task-delete'),
]
