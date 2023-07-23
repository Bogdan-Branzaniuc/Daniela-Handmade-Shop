from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    delivery = 10
    for item_id, size_level in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        for size, color_level in size_level.items():
            for color, qty in color_level.items():
                total += int(qty) * product.price
                bag_items.append({
                    'item_id': item_id,
                    'size': size,
                    'color': product.colors.get(name_EN=color),
                    'quantity': qty,
                    'product': product,
                })

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'bag': bag,
        'grand_total': grand_total,
    }

    return context
