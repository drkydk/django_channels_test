from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ('session_id',)

    def save_model(self, request, obj, form, change):
        obj.session_id = request.session.session_key
        super(ProductAdmin, self).save_model(request, obj, form, change)
