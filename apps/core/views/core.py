"""Core views."""

# Django
from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    """Home page view."""

    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        """Add custom title page home."""

        context = super().get_context_data(**kwargs)
        context['title'] = "jorgesaw"
        return context

class AboutPageView(TemplateView):
    """About page view."""

    template_name = "core/about.html"

    def get_context_data(self, **kwargs):
        """Add custom title page about."""

        context = super().get_context_data(**kwargs)
        context['title'] = "Acerca de"
        return context