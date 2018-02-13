from django.http import Http404
from django.shortcuts import render

from django.utils import translation

from stroykapremont import settings
from .models import Projects, Project_Images


def page(request):
    language = translation.get_language_from_request(request, check_path=True)
    translation.activate(language)
    request.LANGUAGE_CODE = translation.get_language()

    data = dict()

    projects = Projects.objects.all()
    projects_images = Project_Images.objects.all()

    # try:
    #     portfolio = Projects.objects.all()
    # except Projects.DoesNotExist:
    #     raise Http404("Poll does not exist")
    return render(request, 'page.html', {'data': data,
                                         'projects': projects,
                                         'projects_images': projects_images,
                                         })


def home(request):
    return render(request, 'language_select.html')
