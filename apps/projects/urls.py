"""Projects  URLs."""

# Django
from django.urls import include, path

# Views
from .views import projects as projects_views


urlpatterns = [
    path('projects/', projects_views.ProjectListView.as_view(), name="projects"),
]
