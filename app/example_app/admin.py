from django.contrib import admin
from django.contrib import admin
from .models import *

@admin.register(TelUser)
class TelUserAdmin(admin.ModelAdmin):
    pass

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

@admin.register(ConfirmChannel)
class ConfirmChannelAdmin(admin.ModelAdmin):
    pass

class ProductImageInline(admin.TabularInline):
    model = ProductMedia
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    pass