from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Category, AvailableSize, AvailableColor
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
import ast


def products(request, category_name):
    '''
    A view to return the home page index.html
    '''

    if category_name == 'All':
        products = Product.objects.all()
    else:
        category = get_object_or_404(Category, name=category_name)
        products = Product.objects.filter(category=category)

    available_rgba_colors = {}
    for color_instance in AvailableColor.objects.all():
        hex_code = color_instance.hexcolor.replace('#', '')
        rgba_one = []
        rgba_zero = []
        for i in (0, 2, 4):
            decimal = int(hex_code[i:i + 2], 16)
            rgba_one.append(decimal)
            rgba_zero.append(decimal)
        rgba_one.append(0.15)
        rgba_zero.append(0)
        rgba1 = tuple(rgba_one)
        rgba0 = tuple(rgba_zero)
        available_rgba_colors[color_instance.name_EN] = {
            'op_one': f'rgba{rgba1}',
            'op_zero': f'rgba{rgba0}',
        }

    size_units = {
        '0-6': 'months',
        '6-12': 'months',
        '12-18': 'months',
        '18-24': 'months',
        '2-4': 'years',
        '24-30': 'EU',
        '30-35': 'EU',
        '35-38': 'EU',
        '38-43': 'EU',
    }

    context = {
        'products': products,
        'category_name': category_name,
        'available_rgba_colors': available_rgba_colors,
        'size_units': size_units,
    }

    return render(request, 'products/products.html', context)


@login_required
def admin_crud_products(request):
    """

    """
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/admin_crud_products.html', context)


@login_required
def add_product(request):
    """
        A view that handles add product and returns products/add_product_sizes_colors_categories.html page
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product_sizes = ast.literal_eval(
                request.POST.get('extra_field_sizes'))
            if AvailableSize.objects.filter(size__in=product_sizes).count() == len(product_sizes):
                size_instances = AvailableSize.objects.filter(
                    size__in=product_sizes)
                product = form.save()
                product.sizes.set(size_instances)
                product.save()
                messages.success(request, 'Successfully added product!')
                return redirect(reverse('admin_crud_products'))
        else:
            messages.error(
                request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    context = {
        'form': form,
    }

    return render(request, 'products/add_product_sizes_colors_categories.html', context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, ask your supervisor to do this action')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            new_product_sizes = ast.literal_eval(
                request.POST.get('extra_field_sizes'))
            if AvailableSize.objects.filter(size__in=new_product_sizes).count() == len(new_product_sizes):
                size_instances = AvailableSize.objects.filter(
                    size__in=new_product_sizes)
                form.save()
                product.sizes.set(size_instances)
                product.save()
                messages.success(request, 'Successfully updated product!')
                return redirect(reverse('admin_crud_products'))

            return redirect(reverse('admin_crud_products'))
        else:
            messages.error(
                request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
