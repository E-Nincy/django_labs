from django.contrib import admin
from django.urls import path
from learning_logs import views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
]
