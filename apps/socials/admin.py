"""Socials admin."""

# Django
from django.contrib import admin

# Models
from apps.socials.models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
	"""Link admin."""

	fields = ('key', 'name', 'url', 'icon_class_css', 'order')
	readonly_fields = ('created', 'modified')
	list_display = ('name', 'order')
	list_editable = ('order',)
	search_fields = ('name',)
