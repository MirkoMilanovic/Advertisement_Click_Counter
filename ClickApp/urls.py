from django.urls import path
from ClickApp import views


urlpatterns = [
    path('click', views.clickApi, name='click'),
    path('clickTime', views.clickTimeApi, name='click_time'),
]
