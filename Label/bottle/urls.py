from django.urls import path
from . import views

app_name = 'bottle'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('entries/', views.home, name='home'),
    path('upload/', views.upload_entry, name='upload'),
    path('entry/<int:pk>/', views.detail, name='detail'),
]
