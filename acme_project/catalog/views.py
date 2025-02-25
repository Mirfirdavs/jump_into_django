from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def product_category(request, category):
    return HttpResponse(f'Категория {category}')

def product_list(request):
    template_name = 'catalog/product_list.html'
    title = 'Список товаров ACME'
    products = [
        'Iron carrot',
        'Giant mousetrap',  
        'Dehydrated boulders',
        'Invisible paint',
    ]
    context = {
        'title': title,
        'products': products,
    }
    return render(request, template_name, context)

def product_detail(request, pk):
    return HttpResponse('Its dummy response {pk=}')