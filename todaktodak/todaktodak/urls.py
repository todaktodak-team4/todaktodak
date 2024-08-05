from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin4242/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('',include('rememberTree.urls')),
    path('', include('memorialHall.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]

if settings.DEBUG:
    # urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
