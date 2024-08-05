from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.static import serve

urlpatterns = [
    path('admin4242/', admin.site.urls),
    path('accounts/', include('accounts.urls')), # 추가
    path('',include('rememberTree.urls')),
    path('', include('memorialHall.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

