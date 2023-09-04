from django.contrib import admin
from .models import Product,Category,ProductImage,ColorVariant,SizeVariant,Coupon
# Register your models here.

admin.site.register(Category)
admin.site.register(Coupon)


class ProductImageAdmin(admin.StackedInline):
    model =ProductImage
admin.site.register(ProductImage)

@admin.register(ColorVariant)
class ColorVariantAdmin(admin.ModelAdmin):
    list_display = ['color_name' , 'price']
    model = ColorVariant

@admin.register(SizeVariant)
class SizeVariantAdmin(admin.ModelAdmin):
    list_display = ['size_name' , 'price']

    model = SizeVariant


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name' , 'price' ]
    inlines = [ProductImageAdmin]
admin.site.register(Product ,ProductAdmin)




