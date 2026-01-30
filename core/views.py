from django.shortcuts import render
from .models import Skill, Education, CertificationStat
from updates.models import Update

def home(request):
    return render(request, 'core/home.html')


def education(request):
    education_list = Education.objects.all()
    return render(request, 'core/education.html', {'education_list': education_list})

def contact(request):
    return render(request, 'contact/contact.html')




def skills(request):
    skills = Skill.objects.all()
    return render(request, 'core/skills.html', {'skills': skills})


def education(request):
    education_list = Education.objects.all()
    stats = CertificationStat.objects.all()
    return render(request, 'core/education.html', {
        'education_list': education_list,
        'stats': stats
    })


def home(request):
    updates = Update.objects.filter(is_published=True)[:3]
    return render(request, 'core/home.html', {
        'updates': updates
    })

