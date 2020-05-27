"""Projects moddels."""

# Django
from django.db import models

# ckeditor
from ckeditor.fields import RichTextField


class Project(models.Model):
	"""Project class."""

	title = models.CharField(max_length=150, verbose_name='Título')
	subtitle = models.CharField(
		'Subtítulo', 
		max_length=255, 
		null=True, 
		blank=True
	)
	content = RichTextField('Contenido')
	order = models.PositiveSmallIntegerField('Orden', default=0)
	image = models.ImageField('Imagen', upload_to='projects')
	url_code = models.URLField('URL código', max_length=255)
	created = models.DateTimeField('Fecha de creación', auto_now_add=True)
	modified = models.DateTimeField('Ultima edición', auto_now=True)

	class Meta:
		"""Meta class."""

		ordering = ['order', '-id']
		verbose_name = 'Proyecto'

	def __str__(self):
		return self.title
