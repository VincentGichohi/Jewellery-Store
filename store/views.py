from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Address, Cart, Category, Order, Product
from .forms import RegistrationForm, AddressForm
from django.views import View
import decimal
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator # For class based views


def home(request):
    categories = Category.objects.filter(is_active=True, is_featured=True)[:3]
    products = Product.objects.filter(is_active=True, is_featured=True)[:8]
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'store/index.html', context)

