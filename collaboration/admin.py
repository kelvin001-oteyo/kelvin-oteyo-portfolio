from django.contrib import admin
from .models import Collaborator, SharedNote
from django.core.mail import send_mail
from django.conf import settings

@admin.register(Collaborator)
class CollaboratorAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'area', 'date_joined')
    search_fields = ('name', 'email')
    list_filter = ('role', 'area')


@admin.register(SharedNote)
class SharedNoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_by', 'upload_date')



def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        emails = Collaborator.objects.values_list('email', flat=True)

        send_mail(
            'New Shared Note Available',
            f'{obj.title} has been uploaded.',
            settings.DEFAULT_FROM_EMAIL,
            list(emails),
        )