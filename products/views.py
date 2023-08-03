from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProductForm, AvailableSizesForm

def products(request):
    '''
    A view to return the home page index.html
    '''
    products = Product.objects.all()
    
    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


@login_required
def admin_crud_products(request):
    """
    A view that handles add product and returns products/admin_crud_products.html page
    AddAvailableSizesForm, AddAvailableColorsForm and AddCategoryForm will be handled through django-unicorn
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('admin_crud_products'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    context = {
        'form': form,
    }

    return render(request, 'products/admin_crud_products.html', context)

