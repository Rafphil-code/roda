from django_unicorn.components import UnicornView
from core.models import Service

class ServicesView(UnicornView):
    services = []
    visible_count = 3  # nombre de services visibles au départ

    def mount(self):
        # Charger tous les services
        self.services = list(Service.objects.all())

    def load_more(self):
        # augmenter le nombre de services visibles
        print("c'est clicked")
        self.visible_count += 3
        
    def load_less(self):
        self.visible_count -= 3