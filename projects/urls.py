from django.urls import path

from projects.views import ProjectListView, ProjectCreateView, ProjectUpdateView

urlpatterns = [
    path('', ProjectListView.as_view(), name='projects-list'),
    path('add/', ProjectCreateView.as_view(), name='projects-create'),
    path('update/<uuid:pk>/', ProjectUpdateView.as_view(), name='projects-update'),
]
