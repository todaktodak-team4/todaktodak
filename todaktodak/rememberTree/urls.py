from django.urls import path
from .views import TreeAPIView,PhotoAPIView,DailyQuestionAPIView,GetTodayAnswersAPIView,LettersAPIView

urlpatterns = [
    path('rememberTree/', TreeAPIView.as_view()),
    path('rememberTree/<int:pk>/', TreeAPIView.as_view()),
    path('rememberTree/<int:tree_id>/photos/', PhotoAPIView.as_view(), name='photo-list'),
    path('rememberTree/<int:tree_id>/photos/<int:pk>/', PhotoAPIView.as_view(), name='photo-detail'),
    path('rememberTree/daily-question/', DailyQuestionAPIView.as_view(), name='daily-question'),
    path('daily-question/today-answers/', GetTodayAnswersAPIView.as_view(), name='today-answers'),
    path('rememberTree/<int:tree_id>/letters/', LettersAPIView.as_view(), name='letters-list'),
    path('rememberTree/<int:tree_id>/letters/<int:pk>/', LettersAPIView.as_view(), name='letters-detail'),
]
