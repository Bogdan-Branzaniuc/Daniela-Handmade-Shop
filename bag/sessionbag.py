from django.shortcuts import get_object_or_404
from products.models import Product
from django.conf import settings
from decimal import Decimal


def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
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

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'product_count': product_count,
        'bag': bag,
        'total': total,
        'grand_total': grand_total,
        'delivery': round(delivery, 2),
        'delivery_treshold': settings.FREE_DELIVERY_THRESHOLD,
        'left_till_free': settings.FREE_DELIVERY_THRESHOLD - total,
    }

    return context
