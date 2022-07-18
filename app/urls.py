from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get_image/<slug:image_name>', views.show_image, name='show specified image'),
    path('get_image/', views.show_default_image, name='shows default image')
]
