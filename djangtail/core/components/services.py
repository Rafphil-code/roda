from django_unicorn.components import UnicornView
from core.models import Service
from django.urls import reverse
from django.shortcuts import redirect

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
        self.mount()
        
    def load_less(self):
        self.visible_count -= 3
        self.mount()
    
    def go_to_service(self, service_id):
        return redirect(reverse("get_service_filtered", args=[service_id]))
