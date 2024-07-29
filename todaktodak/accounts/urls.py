from django.urls import path,include
from .views import RegisterStepOne, RegisterStepTwo, CustomAuthToken, ProfileUpdateView,google_login,google_callback

urlpatterns = [
    path('register/step1/', RegisterStepOne.as_view(), name='register_step_one'),
    path('register/step2/', RegisterStepTwo.as_view(), name='register_step_two'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path("account/", include("allauth.urls")),
    path("google/login/", google_login, name="google_login"),
    path("google/callback/", google_callback, name="google_callback"),
]

