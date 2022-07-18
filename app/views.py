import os
from django.http import HttpResponse, FileResponse

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def home(request):
    return HttpResponse('Home page')

def show_default_image(request):
    IMG = 'imgaes/media/default.gif'
    PATH = os.path.join(BASE_DIR, IMG)

    image_data = open(PATH, 'rb')

    return FileResponse(image_data)

def show_image(request, image_name='Tomato.png'):
    if image_name == 'tomato':
        image_name = 'Tomato.png'
    elif image_name == 'japan':
        image_name = 'maxresdefault.jpg'
    IMG = 'imgaes/media/' + image_name
    PATH = os.path.join(BASE_DIR, IMG)

    image_data = open(PATH, 'rb')

    return FileResponse(image_data)
