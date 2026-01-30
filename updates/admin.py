from django.contrib import admin
from .models import Update


@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published')
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title', 'summary', 'content', 'meta_description')
