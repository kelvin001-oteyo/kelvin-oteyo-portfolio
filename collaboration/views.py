from os import name
from django.shortcuts import render, redirect
from .models import Collaborator, SharedNote
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings


def collaborate(request):
    if request.method == "POST":
        collaborator_name = request.POST['name']
        collaborator_role = request.POST['role']
        Collaborator.objects.create(
            name=collaborator_name,
            email=request.POST['email'],
            role=collaborator_role,
            area=request.POST['area'],
            message=request.POST['message']
        )

        send_mail(
           subject='New Collaboration Request',
            message=f'New collaborator: {collaborator_name} ({collaborator_role})',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.EMAIL_HOST_USER],
)
        messages.success(request, "You have successfully joined the collaboration.")
        return redirect('collaborate')

    collaborators = Collaborator.objects.all().order_by('-date_joined')
    notes = SharedNote.objects.all().order_by('-upload_date')

    return render(request, 'collaboration/collaborate.html', {
        'collaborators': collaborators,
        'notes': notes
    })





@login_required
def dashboard(request):
    collaborator = Collaborator.objects.filter(
        email=request.user.email
    ).first()

    notes = SharedNote.objects.all().order_by('-upload_date')

    return render(request, 'collaboration/dashboard.html', {
        'collaborator': collaborator,
        'notes': notes
    })

