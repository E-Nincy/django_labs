from django.shortcuts import render, get_object_or_404
from .models import Project

def index(request):
    projects_list = Project.objects.all().order_by('-id')
    context = {'projects': projects_list}
    return render(request, 'projects/index.html', context)

def detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    context = {'project': project}
    return render(request, 'projects/detail.html', context)
