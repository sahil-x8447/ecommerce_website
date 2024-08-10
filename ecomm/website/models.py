from django.db import models
import datetime
from django.contrib.auth.models import User  # Import the User model

# Product categories
class Category(models.Model):
    name = models.CharField(max_length=60)  # Category name

    def __str__(self):
        return self.name
    

# Customers
class Customer(models.Model):
    first_name = models.CharField(max_length=60)  # Customer's first name
    last_name = models.CharField(max_length=60)  # Customer's last name
    phone = models.CharField(max_length=10)  # Customer's phone number
    email = models.EmailField(max_length=100)  # Customer's email address
    password = models.CharField(max_length=100)  # Customer's password

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# Products
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # ForeignKey to Category
    name = models.CharField(max_length=100)  # Product name
    description = models.TextField()  # Product description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Product price
    stock = models.PositiveIntegerField()  # Quantity in stock
    image = models.ImageField(upload_to='uploads/products/')  # Product image
    is_popular = models.BooleanField(default=False)  # Indicator for popular products
    is_new_arrival = models.BooleanField(default=False)  # Indicator for new arrivals

    def __str__(self):
        return self.name


# Orders
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # ForeignKey to Customer
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # ForeignKey to Product
    quantity = models.PositiveIntegerField()  # Quantity of the product ordered
    order_date = models.DateTimeField(default=datetime.datetime.now)  # Date and time of the order
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Total price of the order

    # Address field
    address = models.CharField(max_length=255)  # Shipping address

    # Phone field
    phone = models.CharField(max_length=15)  # Contact phone number

    # Status field
    status = models.BooleanField(default=False)  # Order status (e.g., processed or not)

    def __str__(self):
        return f'Order {self.id} for {self.product.name}'


# Shopping Cart
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # ForeignKey to User
    created_at = models.DateTimeField(auto_now_add=True)  # Creation date of the cart

    def __str__(self):
        return f'Cart for {self.user.username}'


# Cart Items
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)  # ForeignKey to Cart
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # ForeignKey to Product
    quantity = models.PositiveIntegerField()  # Quantity of the product in the cart

    def __str__(self):
        return f'{self.quantity} of {self.product.name}'
    
    @property
    def total_price(self):
        return self.product.price * self.quantity  # Total price for this cart item
