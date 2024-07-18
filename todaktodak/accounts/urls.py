from django.urls import path
from .views import RegisterStepOne, RegisterStepTwo, CustomAuthToken, ProfileUpdateView

urlpatterns = [
    path('register/step1/', RegisterStepOne.as_view(), name='register_step_one'),
    path('register/step2/', RegisterStepTwo.as_view(), name='register_step_two'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
]

