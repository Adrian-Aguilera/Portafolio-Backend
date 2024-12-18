from django.urls import path
from .views import PortafolioMethods
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('projects', PortafolioMethods.get_projects, name='projects'),
    path('works', PortafolioMethods.get_works, name='works'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)