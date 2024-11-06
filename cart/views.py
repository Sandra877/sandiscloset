# views.py in the cart app
from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem
from products.models import Product
from .models import Cart  # Import the Cart model
from django.contrib.auth.decorators import login_required

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)  # Access items through the cart
    total_price = sum(item.total_price() for item in cart_items)
    return render(request, 'cart/cart_detail.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # Assuming each user has a single Cart instance, retrieve the cart for the logged-in user
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Use the cart instance when creating or getting the CartItem
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    # Update the quantity if the item already exists in the cart
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('cart:cart_detail')

@login_required
def remove_from_cart(request, item_id):
    # Get the cart for the current user
    cart = get_object_or_404(Cart, user=request.user)
    
    # Retrieve the CartItem using the cart and item ID
    cart_item = get_object_or_404(CartItem, cart=cart, id=item_id)
    
    # Delete the item from the cart
    cart_item.delete()
    
    # Redirect to the cart detail page or any desired page
    return redirect('cart:cart_detail')
