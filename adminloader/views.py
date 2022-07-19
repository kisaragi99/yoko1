from django.shortcuts import render, redirect
from .models import Category, Title

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def main_page(request):
    category = request.GET.get('category')
    if category == None:
        titles = Title.objects.all()
    else:
        titles = Title.objects.filter(category__name=category)
        
    categories = Category.objects.all()

    context = {'categories': categories, 'titles': titles}
    return render(request, 'manga_admin/main_page.html', context)



def add_chapter(request, title):
    title_id = Title.objects.get(id=title)
    return render(request, 'manga_admin/add_chapter.html', {'title': title_id})



@csrf_exempt
def add_manga(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        title_pic = request.FILES.get('title_pic')

        print('data:', data)
        print('title_pic:', title_pic)

        if data['title_category'] != 'none':
            category = Category.objects.get(id=data['title_category'])
        elif data['title_category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['title_category_new'])
        else:
            category = None

        title = Title.objects.create(
            title_name = data['title_name'],
            pic = title_pic,
            category = category,
        )

        return redirect('main')

    context = {'categories': categories}
    return render(request, 'manga_admin/add_manga.html', context)