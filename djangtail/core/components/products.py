from django_unicorn.components import UnicornView
from core.models import Product


class ProductsView(UnicornView):
    visible_count = 4
    products = []

    def mount(self):
        # Charger tous les services
        self.products = Product.objects.filter(popular=True)

    def load_more(self):
        # augmenter le nombre de services visibles
        print("c'est clicked")
        self.visible_count += 4
        
    def load_less(self):
        self.visible_count -= 4

    def go_to_product(self):
        return self.redirect("products/")
