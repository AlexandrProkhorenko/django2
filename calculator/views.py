from django.http import HttpResponse
from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}







def omlet(request):
    serving = int(request.Get.get('serving',1))
    template_name = 'calculator/index.html'
    context = {
       'recipe': {
         'яйца шт': 2 * serving,
         'Молоко л': 0.1 * serving,
         'соль, ч.л.': 0.5 * serving,
       }
     }


    return (request, template_name, context)


def pasta(request):
    serving = request.Get.get('serving')

    template_name = 'calculator/index.html'
    context = {
       'recipe': {
         'макароны, г': 0.3 * serving,
         'сыр, г': 0.05 * serving,
       }
     }


    return render(request, template_name, context)


def buter(request):
    serving = request.Get.get('serving',1)
    template_name = 'calculator/index.html'
    context = {
        'buter': {
        'хлеб, ломтик': 1 * serving,
        'колбаса, ломтик': 1 * serving,
        'сыр, ломтик': 1 * serving,
        'помидор, ломтик': 1 * serving,

        }
    }

    return render(request, template_name, context)





# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
