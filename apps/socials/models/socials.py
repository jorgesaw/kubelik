"""Socials moddels."""

# Django
from django.db import models


class Link(models.Model):
	"""Link class."""

	key = models.SlugField('Nombre clave', max_length=100, unique=True)
	name = models.CharField('Red social', max_length=255)
	url = models.URLField(
		'Enlace', 
		max_length=255,
		null=True, 
		blank=True
	)
	order = models.PositiveSmallIntegerField('Orden', default=0)
	icon_class_css = models.CharField(
		'Icono de clase css',
		max_length=255,
		null=True, 
		blank=True 
	)
	created = models.DateTimeField('Fecha de creación', auto_now_add=True)
	modified = models.DateTimeField('Ultima edición', auto_now=True)

	
	class Meta:
		"""Meta class."""

		ordering = ['name',]
		verbose_name = 'enlace'
		verbose_name_plural = 'enlaces'

	def __str__(self):
		return self.name
