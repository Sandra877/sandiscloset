from django.shortcuts import get_object_or_404, redirect
from .models import Order, OrderItem
from products.models import Product
from django.shortcuts import render


def create_order_from_product(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        order = Order.objects.create(user=request.user)
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=1,  # Default quantity; you can allow users to specify it
            price=product.price
        )
        return redirect('order_success')  # Redirect to the success page

    return redirect('product_detail', pk=product_id)  # Redirect back if GET request

def order_success(request):
    return render(request, 'orders/order_success.html')