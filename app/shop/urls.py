from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
     path('', views.home, name='home'),
     path('<slug:category_slug>/', views.home, name='list_by_category'),
     path('detail/<int:product_id>/', views.product_detail, name='detail'),
     path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
          path('update/<int:product_id>/', views.update_quantity, name='update_quantity'),
     path('cart/', views.cart, name='cart'),
     path('delete/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
]
