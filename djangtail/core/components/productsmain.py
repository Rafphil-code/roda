from django_unicorn.components import UnicornView
from core.models import Product, Category
from django.core.paginator import Paginator


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
    
    def mount(self):
        self.categories = list(Category.objects.all())
        self.load_products()
    
    def load_products(self):
        qs = Product.objects.all()

        if self.category_id:
            qs = qs.filter(category_id=self.category_id)
        
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


