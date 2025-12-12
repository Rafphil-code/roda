from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import F
from django.core.paginator import Paginator
from django.core.validators import validate_email

# Create your views here.

def index(request):
    products_vogue = Product.objects.filter(popular=True)
    services = Service.objects.all()
    return render(request, 'main.html', { 'services' : services})

def send_email(request):
    print("called")
    if request.method == "POST":
        email = request.POST.get('mail','').strip()
        name = request.POST.get('name','').strip()
        message = request.POST.get('message','').strip()
        if not email or not name or not message:
            messages.error(request, "Tous les champs sont obligatoires !")
            return redirect("index")
        else:
            valide_mail = validate_email(email)
            if valide_mail == None:
                object = f"MESSAGE DE {name} ! Voici mon Mail : {email}"
                sender = settings.EMAIL_HOST_USER
                receiver = [settings.EMAIL_HOST_USER]
                sent_status = send_mail(
                    object,
                    message,
                    sender,
                    receiver,
                    fail_silently=True
                )
            else:
                messages.error(request, "Corrigeez votre Mail puis réessayez !")
        if sent_status == 1:
            messages.success(request, "Email envoyé!")
        return redirect("index")
    

def products(request):

    products = Product.objects.all()

    categories = Category.objects.all()

    paginator = Paginator(products, 5)  # 4 produits par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'products.html')

"""def product_modal(request, pk):
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
"""

def services(request):
    all_services = Service.objects.all()
    return render(request, 'services.html', {'services' : all_services})

def get_service_filtered(request, id):
    service = Service.objects.get(id = id)
    return render(request, 'service.html', {'service' : service})

@login_required
def carts(request):
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

def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            messages.success(request, f"Bienvenue {user.username}")
            return redirect('index')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "Vous êtes bien déconnecté")
    return redirect('index')

def sign_in(request):
    return render(request, 'sign_in.html')

def sign_in_validator(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'sign_in.html', {"error" : "L'utilisateur Existe déjà"})
        if User.objects.filter(email=email).exists():
            return render(request, 'sign_in.html', {"error" : "L'utilisateur Existe déjà"})
        
        user = User.objects.create_user(username=username,email=email,password=password)
    return redirect('login')

