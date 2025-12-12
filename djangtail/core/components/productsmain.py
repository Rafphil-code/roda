from django_unicorn.components import UnicornView
from core.models import Product, Category
from django.core.paginator import Paginator
from django.urls import reverse
from django.shortcuts import redirect


class ProductsmainView(UnicornView):
    products = [] #n'est plus utilisé
    categories = []
    category_id:int = None
    page_obj = None
    page = 1
    has_next: bool = False
    has_previous: bool = False
    page_range:list = []
    total_pages: int = 1
    display_modal:bool = False
    modal_product = []
    modal_product_id:int = None
    
    def mount(self):
        self.categories = list(Category.objects.all())
        self.products = list(Product.objects.all())
        self.load_products()
    
    def load_products(self):
        qs = Product.objects.all()

        if self.category_id:
            qs = qs.filter(category_id=self.category_id)
        if self.category_id == 0:
            qs = Product.objects.all()
        
        paginator = Paginator(qs, 6)
        page_actu = paginator.get_page(self.page)

        # Produits visibles
        self.products = list(page_actu.object_list)

        # Infos de pagination sérialisables
        self.has_next = page_actu.has_next()
        self.has_previous = page_actu.has_previous()
        self.page_range = list(page_actu.paginator.page_range)
        self.total_pages = page_actu.paginator.num_pages
        self.page = page_actu.number    


    def update_category(self):
        self.page = 1
        self.load_products()
        self.categories = list(Category.objects.all())

    def change_page(self, page_number):
        self.page = page_number
        self.load_products()
        self.categories = list(Category.objects.all())

    def view_modal(self, mod_product_id):
        self.modal_product_id = mod_product_id
        self.modal_product = Product.objects.get(id=self.modal_product_id)
        self.display_modal = True
        self.mount()
    
    def close_modal(self):
        self.display_modal = False
        self.mount()
        


    def add_to_cart(self, product_id):
        return redirect(reverse("add_to_cart", args=[product_id]))


