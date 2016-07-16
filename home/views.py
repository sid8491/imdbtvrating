from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from .models import HireMe, Suggestion, Projects


def home(request):
    return render(request, 'home/home.html')


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


def projects(request):
    context = {
        'context1': Projects.objects.all()
    }
    return render(request, 'home/projects.html', context)


def projects_details(request):
    pass
    # try:
        # checkfromdb = ShowDetail.objects.get(title=project_name)


def suggestions(request):
    return render(request, 'home/suggestions.html')


def suggestionssubmit(request):
    sug = Suggestion()
    sug.name = str(request.POST['name'])
    sug.email = str(request.POST['email'])
    sug.suggestion = str(request.POST['suggestion'])
    sug.save()
    return HttpResponseRedirect(reverse('suggestions'))


def contactus(request):
    return render(request, 'home/contactus.html')


