from django.urls import path

from . import views

urlpatterns = [
    path('helloworld/', views.helloworld),
    path('', views.homePage, name='home-page'),
    path('yourname/<str:name>', views.yourName, name='your-name')
]
