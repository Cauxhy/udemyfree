# products/views.py
import random
from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator

def home(request):
    search_query = request.GET.get('search', '')
    selected_category = request.GET.get('category', None)

    products = Product.objects.all()

    # Filtrer par catégorie si une catégorie est sélectionnée
    if selected_category and selected_category != 'None':
        products = products.filter(category_id=selected_category)

    # Filtrer par recherche
    if search_query:
        products = products.filter(title__icontains=search_query)

    # Pagination
    paginator = Paginator(products, 21)  # 20 produits par page
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    # Récupérer toutes les catégories pour le filtre
    categories = Category.objects.all()

    return render(request, 'products/home.html', {
        'products': products,
        'categories': categories,
        'search_query': search_query,
        'selected_category': selected_category,
    })


def product_list(request):
    search_query = request.GET.get('search', '')
    selected_category = request.GET.get('category', None)

    products = Product.objects.all()

    # Filtrer par catégorie si une catégorie est sélectionnée
    if selected_category and selected_category != 'None':
        products = products.filter(category_id=selected_category)

    # Filtrer par recherche
    if search_query:
        products = products.filter(title__icontains=search_query)

    # Pagination
    paginator = Paginator(products, 21)  # 21 produits par page
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    # Récupérer toutes les catégories pour le filtre
    categories = Category.objects.all()

    # Récupérer 6 produits aléatoires
    random_courses = Product.objects.order_by('?')[:6]

    return render(request, 'products/product_list.html', {
        'products': products,
        'categories': categories,
        'search_query': search_query,
        'selected_category': selected_category,
        'random_courses': random_courses,  # Ajoutez ceci pour passer les cours aléatoires au template
    })
    
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    # Récupérer tous les produits et choisir 6 aléatoires
    all_courses = list(Product.objects.all())
    random_courses = random.sample(all_courses, min(8, len(all_courses)))

    return render(request, 'products/product_detail.html', {
        'product': product,
        'random_courses': random_courses
    })
    
def how_to_use(request):
    return render(request, 'products/how_to_use.html', {})