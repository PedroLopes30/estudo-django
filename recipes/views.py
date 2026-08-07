from django.shortcuts import render, get_object_or_404, get_list_or_404
from utils.recipes.factory import make_recipe
from django.http import Http404
from .models import Recipe

def home (request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request,'recipes/pages/home.html', {
        'recipes': recipes,
    })

def category (request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')

    if not recipes:
        raise Http404('Not found :(')
    
    return render(request,'recipes/pages/category.html', {
        'recipes': recipes,
        'title': f'{recipes.first().category.name} - Category | '
    })

def recipe (request, id):
    recipe = get_object_or_404(Recipe, pk=id)

    return render(request,'recipes/pages/recipe-view.html', {
        'recipe': recipe,
        'is_detail_page': True
    })  