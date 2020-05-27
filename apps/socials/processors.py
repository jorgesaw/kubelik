"""Socials processors"""

# Django

# Models
from apps.socials.models import Link

def context_socials_links(request):
	"""Add links models data at processors context."""

	links = Link.objects.all()
	context = {'links': links}

	return context
