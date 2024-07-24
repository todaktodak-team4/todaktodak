from rest_framework.routers import SimpleRouter
from django.urls import path, include
from .views import MemorialHallViewSet, WreathViewSet, MessageViewSet

memorialHall_router = SimpleRouter(trailing_slash=False)
memorialHall_router.register('memorialHall', MemorialHallViewSet, basename='memorialHall')

wreath_router = SimpleRouter(trailing_slash=False)
wreath_router.register('wreath', WreathViewSet, basename='wreath')

message_router = SimpleRouter(trailing_slash=False)
message_router.register('message', MessageViewSet, basename='message')

urlpatterns = [
    path('', include(memorialHall_router.urls)),
    path('memorialHall/<int:pk>/participate/', MemorialHallViewSet.as_view({'post': 'participate'}), name='memorialhall-participate'),
    path('memorialHall/<int:pk>/unparticipate/', MemorialHallViewSet.as_view({'post': 'unparticipate'}), name='memorialhall-unparticipate'),
    path('memorialHall/<int:pk>/access/', MemorialHallViewSet.as_view({'get': 'access_private_hall'}), name='memorialhall-access-private'),
    path('memorialHall/<int:memorialHall_id>/', include(wreath_router.urls)),
    path('memorialHall/<int:memorialHall_id>/', include(message_router.urls)),
]