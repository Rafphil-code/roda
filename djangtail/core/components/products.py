from django_unicorn.components import UnicornView
from core.models import Product


class ProductsView(UnicornView):
    visible_count = 4
    products = []
    modal_product = []
    modal_product_id:int = None
    display_modal:bool = False

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
    
    def show_modal(self, product_id):
        print("SHOW MODAL TRIGGERED AVEC :", product_id)
        self.modal_product_id = product_id
        self.modal_product = Product.objects.get(id=self.modal_product_id)
        self.display_modal = True
    
    def close_modal(self):
        self.display_modal = False
