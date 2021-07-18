from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
    list_display_links = ["name", "created_at", "updated_at"]
    search_fields = ["name", "created_at", "updated_at"]

class UserAdmin(admin.ModelAdmin):
    list_display = ["firstname","lastname","email","phone_number","password","is_admin","is_staff","is_superuser"]
    # list_display_links = ["firstname","lastname","email","phone_number","password"]
    search_fields = ["firstname","lastname","email","phone_number","password"]

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name","price","stock","product_description","rating","category","created_at","updated_at","image"]
    list_display_links = ["name","price","stock","product_description","rating","category","created_at","updated_at","image"]
    search_fields = ["name","price","stock","product_description","rating","created_at","updated_at","image"]

admin.site.register(User,UserAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)