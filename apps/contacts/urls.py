"""Contacts  URLs."""

# Django
from django.urls import include, path

# Views
from .views import contacts as contacts_views


urlpatterns = [
    path('contact/', contacts_views.ContactView.as_view(), name="contact"),
]
