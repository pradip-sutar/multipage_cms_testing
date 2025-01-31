from django.contrib import admin
from .models import Menu, Submenu

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'link')
    search_fields = ('title',)

@admin.register(Submenu)
class SubmenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'menu', 'link')
    search_fields = ('title',)
    list_filter = ('menu',)
