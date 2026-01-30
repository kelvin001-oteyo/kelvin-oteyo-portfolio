from django.db import models
from django.contrib.auth.models import User

class Collaborator(models.Model):
    ROLE_CHOICES = [
        ('Student', 'Student'),
        ('Developer', 'Developer'),
        ('Designer', 'Designer'),
        ('Researcher', 'Researcher'),
        ('Other', 'Other'),
    ]

    AREA_CHOICES = [
        ('Projects', 'Projects'),
        ('Notes', 'Notes'),
        ('Research', 'Research'),
        ('Mentorship', 'Mentorship'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    area = models.CharField(max_length=20, choices=AREA_CHOICES)
    message = models.TextField()
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class SharedNote(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='notes/')
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title