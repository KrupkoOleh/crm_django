from django.urls import path

from projects.views import ProjectListView, ProjectCreateView

urlpatterns = [
    path('', ProjectListView.as_view(), name='projects-list'),
    path('add/', ProjectCreateView.as_view(), name='projects-create'),
]
