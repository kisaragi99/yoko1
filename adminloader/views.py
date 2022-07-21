from django.shortcuts import render, redirect
from .models import Category, Title

from django.views.decorators.csrf import csrf_exempt




#Главная страница админки
def main_page(request):
    category = request.GET.get('category')
    if category == None:
        titles = Title.objects.all()
    else:
        titles = Title.objects.filter(category__name=category)

    categories = Category.objects.all()  # для левой менюшки (Статусы)

    context = {'categories': categories, 'titles': titles}
    return render(request, 'manga_admin/main_page.html', context)



# изменить инфу о манге
@csrf_exempt
def change_info(request, title_id):
    title = Title.objects.get(id=title_id)

    new_name = title.name
    new_description = title.description
    new_category = title.category
    new_cover = title.cover

    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        print('data:', data)

        new_name = data['name']
        new_description = data['description']
        new_category = Category.objects.get(id=data['title_category'])
        if (data['cover'] != ''):
            new_cover = data['cover']


        title.name = new_name
        title.description = new_description
        title.category = new_category
        title.save()

        return redirect('change info', title_id)

    return render(request, 'manga_admin/change_info.html', {'title': title, 'categories': categories,})



#добавление новой главы в мангу (несколько файлов)
def add_chapter(request, title_id):
    title = Title.objects.get(id=title_id)

    return render(request, 'manga_admin/add_chapter.html', {'title': title})




# добавление новой манги
@csrf_exempt
def add_manga(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        title_cover = request.FILES.get('title_cover')

        print('data:', data)
        print('title_cover:', title_cover)

        if data['title_category'] != 'none':
            category = Category.objects.get(id=data['title_category'])
        elif data['title_category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['title_category_new'])
        else: 
            category = None

        title = Title.objects.create(
            name = data['name'],
            cover = title_cover,
            category = category,
            description = data['description']
        )

        return redirect('main')

    context = {'categories': categories}
    return render(request, 'manga_admin/add_manga.html', context)