from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from app.cart.forms import CartAddProductForm

def home(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products  = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/home.html', {'products': products, 'category': category, 'categories': categories})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id, available=True)
    cart_form_product = CartAddProductForm()
    return render(request, 'shop/product_detail.html', {'product': product, 'form': cart_form_product})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id, available=True)
    cart = request.session.get('cart', {})
    if product_id not in cart:
        cart[product_id] = {
            'id': product.id,
            'name': product.name,
            'price': str(product.price)
        }
    request.session['cart'] = cart
    return redirect('shop:cart')

def cart(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0
    for product_id, product in cart.items():
        total += float(product['price'])
        products.append(product)
    return render(request, 'shop/cart.html', {'products': products, 'total': total, 'cart': cart})


def update_quantity(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    quantity_str = request.POST.get('quantity')
    if quantity_str and quantity_str.isnumeric():
        quantity = int(quantity_str)
        if quantity > 0:
            if product_id in cart: # vérifier si l'article est dans le panier
                cart[product_id]['quantity'] = quantity
            else:
                # ajouter un nouvel élément au panier
                cart[product_id] = {'quantity': quantity, 'price': str(product.price)}
        else:
            del cart[product_id]
    request.session['cart'] = cart
    return redirect('shop:cart')


def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    del cart['product_id']
    request.session['cart'] = cart
    return redirect('shop:cart')
