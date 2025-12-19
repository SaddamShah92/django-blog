from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request):
    projects = Project.objects.all().order_by('created_at')
    context = {
        'projects' : projects
    }

    return render(request, 'portfolio/project_list.html', context)


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    context = {
        'project' : project
    }

    return render(request, 'portfolio/project_detail.html', context)