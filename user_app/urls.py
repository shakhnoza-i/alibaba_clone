from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from user_app.views import RegistrationView, LogoutView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout')
]
