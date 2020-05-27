"""Projects admin."""

# Django
from django.contrib import admin

# Models
from apps.projects.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	"""Project admin."""

	fields = ('title', 'subtitle', 'order', 'content', 'image', 'url_code')
	readonly_fields = ('created', 'modified')
	list_display = ('title', 'order')
	list_editable = ('order',)
	search_fields = ('title',)
