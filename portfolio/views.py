from django.shortcuts import render
from .models import Education, Experience, Project, Skill


def landing(request):
    """Home / landing page — featured projects."""
    projects = Project.objects.filter(is_featured=True)
    return render(request, 'portfolio/landing.html', {'projects': projects})


def resume(request):
    """Full résumé page."""
    context = {
        'skills': Skill.objects.all(),
        'experiences': Experience.objects.all(),
        'educations': Education.objects.all(),
    }
    return render(request, 'portfolio/resume.html', context)


def contact(request):
    """Simple contact page (no form processing yet)."""
    return render(request, 'portfolio/contact.html')
