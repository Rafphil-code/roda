from django_unicorn.components import UnicornView, QuerySetType
from django.contrib.auth.models import User
from core.models import UserItem
from django.db.models import F

class CartView(UnicornView):
    user_products : QuerySetType[UserItem] = None
    user_pk: int

    def mount(self):
        self.user_pk = self.user = self.component_kwargs.get("user")
        self.user_products = UserItem.objects.filter(user_id=self.user_pk)

