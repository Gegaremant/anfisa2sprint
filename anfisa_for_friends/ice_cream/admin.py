from django.contrib import admin

# Register your models here.
from .models import Category, Topping, Wrapper, IceCream

# admin.site.register(Category)
admin.site.register(Topping)
admin.site.register(Wrapper)
# admin.site.register(IceCream)

# Это свойство сработает для всех полей этой модели.
# Вместо пустого значения будет выводиться строка "Не задано".
admin.site.empty_value_display = 'Не задано'


class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )    
    search_fields = ('title',) 
    list_filter = ('category',)
    list_display_links = ('title',) 

    # Указываем, для каких связанных моделей нужно включить такой интерфейс:
    # Перекладывать из одного в ругое
    filter_horizontal = ('toppings',)


admin.site.register(IceCream, IceCreamAdmin)

# Подготавливаем модель IceCream для вставки на страницу другой модели.
class IceCreamInline(admin.StackedInline):
    model = IceCream
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',        
    )

admin.site.register(Category, CategoryAdmin) 
