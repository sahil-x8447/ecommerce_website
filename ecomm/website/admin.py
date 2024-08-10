from django.contrib import admin
from .models import Category, Customer, Product, Order

# Admin configuration for Category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Fields to display in the list view
    search_fields = ('name',)  # Fields to include in the search functionality

# Admin configuration for Customer model
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'email')  # Fields to display in the list view
    search_fields = ('first_name', 'last_name', 'email')  # Fields to include in the search functionality
    list_filter = ('phone',)  # Fields to filter the list view by

# Admin configuration for Product model
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'stock', 'image')  # Fields to display in the list view
    search_fields = ('name', 'category__name')  # Fields to include in the search functionality
    list_filter = ('category',)  # Fields to filter the list view by

# Admin configuration for Order model
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product', 'quantity', 'order_date', 'total_price', 'address', 'phone', 'status')  # Fields to display in the list view
    search_fields = ('customer__first_name', 'customer__last_name', 'product__name', 'address', 'status')  # Fields to include in the search functionality
    list_filter = ('order_date', 'status')  # Fields to filter the list view by
    list_editable = ('status',)  # Fields that can be edited directly in the list view

# Register models with the admin site
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
    