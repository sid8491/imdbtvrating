from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import HireMe, Suggestion, Projects
from django.views.decorators.cache import never_cache


@never_cache
def home(request):
    return render(request, 'home/home.html')


@never_cache
def hireme(request):
    return render(request, 'home/hire.html')


def hiremesubmit(request):
    hire = HireMe()
    hire.name = str(request.POST['name'])
    hire.email = str(request.POST['email'])
    hire.number = str(request.POST['contact'])
    hire.comments = str(request.POST['comments'])
    hire.save()
    return HttpResponseRedirect(reverse('hireme'))


@never_cache
def projects(request):
    context = {
        'context': Projects.objects.all()
    }
    return render(request, 'home/projects.html', context)


@never_cache
def projects_details(request, project_name):
    context = {
        'code': Projects.objects.filter(name=project_name).values_list('code')
    }
    return render(request, 'home/projects_details.html', context)


@never_cache
def suggestions(request):
    return render(request, 'home/suggestions.html')


def suggestionssubmit(request):
    sug = Suggestion()
    sug.name = str(request.POST['name'])
    sug.email = str(request.POST['email'])
    sug.suggestion = str(request.POST['suggestion'])
    sug.save()
    return HttpResponseRedirect(reverse('suggestions'))


@never_cache
def contactus(request):
    return render(request, 'home/contactus.html')


