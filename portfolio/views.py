from django.shortcuts import get_object_or_404, render
from .models import Certification, Education, Experience, Project, Skill


def landing(request):
    """Home / landing page — featured projects and summary."""
    projects = Project.objects.filter(is_featured=True)
    return render(request, 'portfolio/landing.html', {'projects': projects})


def resume(request):
    """Full résumé page."""
    context = {
        'skills': Skill.objects.all(),
        'experiences': Experience.objects.all(),
        'educations': Education.objects.all(),
        'certifications': Certification.objects.all(),
    }
    return render(request, 'portfolio/resume.html', context)


def projects_list(request):
    """All showcase projects filterable by tool (Power BI, Tableau, Excel)."""
    filter_type = request.GET.get('type')
    projects = Project.objects.all()
    if filter_type:
        projects = projects.filter(project_type=filter_type)
    return render(request, 'portfolio/projects_list.html', {
        'projects': projects,
        'current_type': filter_type,
    })


def project_detail(request, slug):
    """Detail view for a single showcase project (supports embed & file download)."""
    project = get_object_or_404(Project, slug=slug)
    highlights = [h.strip() for h in project.key_highlights.split('\n') if h.strip()]
    return render(request, 'portfolio/project_detail.html', {
        'project': project,
        'highlights': highlights,
    })


def contact(request):
    """Contact page with direct links and details."""
    return render(request, 'portfolio/contact.html')
