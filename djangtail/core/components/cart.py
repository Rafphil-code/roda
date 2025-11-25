from django_unicorn.components import UnicornView, QuerySetType
from django.contrib.auth.models import User
from core.models import UserItem
from django.db.models import F

class CartView(UnicornView):
    user_products : QuerySetType[UserItem] = None
    user_pk: int

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.user_pk = kwargs.get('user')
        #self.user_products = UserItem.objects.filter(user=self.user_pk)
        self.user_products = UserItem.objects.all()
