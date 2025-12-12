from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sendmail', views.send_email, name='send_email'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('sign_in_validator', views.sign_in_validator, name='sign_in_validator'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('products', views.products, name='products'),
    path('cart_all', views.carts, name='carts'),
    #path('products/filter', views.category_show, name='toggle_filters'),
    path('products/add_to_cart/<int:product_id>', views.add_item, name='add_to_cart'),
    #path('product_modal/<int:pk>', views.product_modal, name='product_modal'),
    #path('products/<str:category_name>/', views.filter_by_category, name='filter_by_category'),
    path('services', views.services, name='services'),
    path('services/<int:id>', views.get_service_filtered, name='get_service_filtered'),
]
