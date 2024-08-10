from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartItem
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

# Home page view displaying all products
def home(request):
    products = Product.objects.all()  # Retrieve all products from the database
    return render(request, 'home.html', {'products': products})

# About page view
def about(request):
    return render(request, 'about.html')

# Login view for users
def login_user(request):
    if request.method == 'POST':  # Check if the request method is POST
        username = request.POST.get('username')  # Get username from POST data
        password = request.POST.get('password')  # Get password from POST data
        user = authenticate(request, username=username, password=password)  # Authenticate user
        if user is not None:  # Check if authentication was successful
            login(request, user)  # Log the user in
            messages.success(request, "You have been successfully logged in.")  # Success message
            return redirect('home')  # Redirect to home page
        else:
            messages.error(request, "Invalid username or password.")  # Error message for failed login
    return render(request, 'login.html')  # Render login page

# Logout view for users
def logout_user(request):
    logout(request)  # Log the user out
    messages.success(request, "You have been successfully logged out.")  # Success message
    return redirect('home')  # Redirect to home page

# Product detail view
def product(request, pk):
    product = get_object_or_404(Product, pk=pk)  # Retrieve product by primary key, or return 404 if not found
    return render(request, 'product.html', {'product': product})  # Render product detail page

# View to display all products
def all_products(request):
    products = Product.objects.all()  # Retrieve all products from the database
    return render(request, 'all_products.html', {'products': products})  # Render all products page

# View for popular items
def popular_items(request):
    # List of IDs for popular items
    popular_ids = [1, 2]  # Example IDs for popular products
    products = Product.objects.filter(id__in=popular_ids)  # Retrieve products with IDs in the popular_ids list
    return render(request, 'popular_items.html', {'products': products})  # Render popular items page

# View for new arrivals
def new_arrivals(request):
    # List of IDs for new arrivals
    new_arrival_ids = [5]  # Example ID for new arrival product
    products = Product.objects.filter(id__in=new_arrival_ids)  # Retrieve products with IDs in the new_arrival_ids list
    return render(request, 'new_arrivals.html', {'products': products})  # Render new arrivals page
