"""Main URLs module."""

from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
    
    # Core app
    path('', include(('apps.core.urls', 'core'), namespace='core')),

    # Projects app
    path('', include(('apps.projects.urls', 'projects'), namespace='projects')),
	
	# Contact app
    path('', include(('apps.contacts.urls', 'contacts'), namespace='contacts')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
