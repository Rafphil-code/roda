from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import F
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    products_vogue = Product.objects.filter(popular=True)
    services = Service.objects.all()
    return render(request, 'main.html', { 'services' : services})

def products(request):

    products = Product.objects.all()

    categories = Category.objects.all()

    paginator = Paginator(products, 5)  # 4 produits par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'products.html')

def product_modal(request, pk):
    print("ok")
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'modal_product.html', {'product': product})

def filter_by_category(request, category_name):
    categories = Category.objects.all()
    try:
        category = Category.objects.get(name__iexact=category_name)
        filtered_products = Product.objects.filter(category=category)
        print(filtered_products)
    except:
        filtered_products = []
        print(f"La catégorie '{category_name}' n'existe pas.")
    return render(request, 'articles.html', {'products' : filtered_products} )


def category_show(request):
    categories = Category.objects.all()
    show_state = request.session.get("show_filters", False)
    new_state = not show_state
    request.session["show_filters"] = new_state
    print(new_state)
    return render(request, 'partials/block_categories.html', {'categories' : categories, "show_filters": new_state})


def services(request):
    all_services = Service.objects.all()
    return render(request, 'services.html', {'services' : all_services})

def get_service_filtered(request, id):
    service = Service.objects.get(id = id)
    return render(request, 'service.html', {'service' : service})

def carts(request):
    user = User.objects.get(username="Philippe")
    login(request, user)
    return render(request, 'cart.html')

@login_required
def add_item(request, product_id):
        product = get_object_or_404(Product, id = product_id)
        user = request.user
        item, created = UserItem.objects.get_or_create(user=user, product=product)
        if not created:
            item.quantity = F('quantity') + 1
            item.save()
        user_products = UserItem.objects.filter(user=user)
        print(user_products)
        return redirect('carts')