from django.contrib import admin
from .models import Business, Category, Purchase

""" @admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ['id','username','title', 'seller','email','number', 'category', 'location', 'price', 'revenue','expense','profit','description','img1','img2']
    list_filter = ['category']
    search_fields = ['title', 'seller']
    
    # Other customizations for the Business model in the admin site

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['type']
    search_fields = ['type']
    # Other customizations for the Category model in the admin site """

admin.site.register(Business)
admin.site.register(Category)
admin.site.register(Purchase)