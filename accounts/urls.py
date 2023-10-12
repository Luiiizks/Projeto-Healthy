from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('register/', views.SignUp.as_view(), name="signup"),
    path('', LoginView.as_view(), name='login'),
    path('home/', login_required(LoginView.as_view(), redirect_field_name=None), name='login'),
    
]
