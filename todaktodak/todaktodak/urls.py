from django.contrib import admin
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin4242/', admin.site.urls),
    path('accounts/', include('accounts.urls')), # 추가
    path('',include('rememberTree.urls')),
    path('', include('memorialHall.urls')),
    re_path(r'^assets/(?P<path>.*)$', serve, { 'document_root': settings.STATIC_ROOT }),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

