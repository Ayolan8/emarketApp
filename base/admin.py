from django.contrib import admin
from .models import Item, Category

class imageAdmin(admin.ModelAdmin):
    list_display = ["title", "photo"]

class categoryAdmin(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(Item, imageAdmin)
admin.site.register(Category, categoryAdmin)
