from django.urls import path, include
from . import views

urlpatterns = [
    path('about/', views.about, name="about"),

    path('dashboard/', views.dashboard, name="dashboard"),

    path('blog/', views.blog, name='blog'),
]