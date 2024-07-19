from django.urls import path
from .views import TreeAPIView

urlpatterns = [
    path('rememberTree/', TreeAPIView.as_view()),
    path('rememberTree/<int:pk>/', TreeAPIView.as_view()),
]
