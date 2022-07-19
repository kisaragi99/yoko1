from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('add/chapter/<str:title>/', views.add_chapter, name='add chapter'),
    path('add/manga/', views.add_manga, name='add manga')
]