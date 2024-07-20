from django.urls import path
from .views import TreeAPIView,PhotoAPIView

urlpatterns = [
    path('rememberTree/', TreeAPIView.as_view()),
    path('rememberTree/<int:pk>/', TreeAPIView.as_view()),
    path('rememberTree/<int:tree_id>/photos/', PhotoAPIView.as_view(), name='photo-list'),
    path('rememberTree/<int:tree_id>/photos/<int:pk>/', PhotoAPIView.as_view(), name='photo-detail'),
]
