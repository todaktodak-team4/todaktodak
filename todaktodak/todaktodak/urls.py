from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.static import serve


urlpatterns = [
    path('admin4242/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/',include('rememberTree.urls')),
    path('api/', include('memorialHall.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^assets/(?P<path>.*)$', serve, { 'document_root': settings.STATIC_ROOT }),
    path('api/', TemplateView.as_view(template_name='index.html')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
