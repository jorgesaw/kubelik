"""Core functionals tests."""

# Django
from django.urls import resolve
from django.test import TestCase
from django.template.loader import render_to_string

from apps.core.views.core import HomePageView


class HomePageTest(TestCase):
	

	def test_root_url_resolves_to_home_page_view(self):
		"""Check rout url at homepage."""

		found = resolve('/')
		self.assertEqual(found.view_name, 'core:home')
		self.assertEqual(found.func.__name__, HomePageView.as_view().__name__)

	def test_home_page_returns_correct_html(self):
		response = self.client.get('/')

		html = response.content.decode('utf-8')
		self.assertTrue(html.startswith('<!DOCTYPE html>\n<html lang="es">'))
		self.assertIn('<title>jorgesaw | Kubelik</title>', html)
		self.assertTrue(html.strip().endswith('</html>'))

	def test_uses_home_template(self):
		response = self.client.get('/')

		self.assertTemplateUsed(response, 'core/home.html')
	

if __name__ == '__main__':
	unittest.main() 