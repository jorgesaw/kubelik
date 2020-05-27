"""Projects views."""

# Django
from django.views.generic.list import ListView

# Models
from apps.projects.models import Project


class ProjectListView(ListView):
	"""Project list view."""

	model = Project
	paginate_by = 10

	def get_context_data(self, **kwargs):
		"""Add custom title page."""

		context = super().get_context_data(**kwargs)
		context['title'] = 'Portfolio'
		return context