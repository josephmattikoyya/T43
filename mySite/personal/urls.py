from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('page2/', views.page2, name='page2'),
    path('page3/', views.page3, name='page3'),
]
