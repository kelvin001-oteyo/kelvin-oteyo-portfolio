from django.contrib import admin
from .models import CollaborationRequest


@admin.register(CollaborationRequest)
class CollaborationAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('user__username',)