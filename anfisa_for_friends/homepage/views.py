from django.shortcuts import render

from ice_cream.models import IceCream


def index(request):
    template_name = 'homepage/index.html'
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'category__title', 'price', 'description'
        ).filter(
            is_on_main=True,
            is_published=True,
            category__is_published=True  # Категория разрешена к публикации.
            )

    context = {
        'ice_cream_list': ice_cream_list,
    }
    # Словарь контекста передаём в шаблон, рендерим HTML-страницу:
    return render(request, template_name, context)
