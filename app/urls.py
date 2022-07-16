import os
from django.contrib import admin
from django.urls import path
from django.http import FileResponse, HttpResponse
from random import randint
value = randint(0, 10)
print(value)

IMG_URL = 'get_image/'
TOMATO_IMG ="imgaes/media/Tomato.png"
JAPAN_IMG = "imgaes/media/maxresdefault.jpg"
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PATH = os.path.join(BASE_DIR, TOMATO_IMG)

def Show_image(request):
    image_data = open(PATH, 'rb')
    return FileResponse(image_data)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(IMG_URL, Show_image),
]