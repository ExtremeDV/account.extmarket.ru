from django.contrib import admin
from .models import Category, Tags, Seller, Product, FeedbackSeller, FeedbackProduct, Certificates

# Register your models here.
admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Seller)
admin.site.register(Product)
admin.site.register(FeedbackSeller)
admin.site.register(FeedbackProduct)
admin.site.register(Certificates)