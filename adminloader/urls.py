from django.urls import path
from . import views

urlpatterns = [
    path('admin-loader/', views.main_page, name='main'),
    path('admin-loader/add-manga/', views.add_manga, name='add manga'),
    path('admin-loader/<str:title_id>/info/', views.change_info, name='change info'),
    path('admin-loader/<str:title_id>/add-chapter/', views.add_chapter, name='add chapter'),
]