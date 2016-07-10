from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import Http404
from .models import ShowDetail
from django.contrib.admin.views.decorators import staff_member_required

import requests
import json


def show(request):
    context = {'all_shows': ShowDetail.objects.all()}
    return render(request, 'show_rating/show.html', context)


def show_detail(request, show_name):
    try:
        detail = ShowDetail.objects.get(title=show_name)
        context = {
            'detail': detail
        }
        return render(request, 'show_rating/details.html', context)
    except ShowDetail.DoesNotExist:
        raise Http404("Wrong show")


def updateshow(request):
    context = {'all_details': ShowDetail.objects.all()}
    return render(request, 'some.html', context)
updateshow = staff_member_required(updateshow)


def updateshowget(request):
    try:
        show1 = get_object_or_404(ShowDetail, title=request.POST['Show'])
    except Exception as e:
        print(e)
    context = getshow(str(show1))
    show1.imdb_id = context['imdbID']
    show1.rating = context['imdbRating']
    show1.raters = context['imdbVotes']
    show1.total_seasons = context['totalSeasons']
    show1.year = context['Year']
    show1.release = context['Released']
    show1.story = context['Plot']
    show1.link = context['Link']
    show1.poster = context['Poster']

    # show.link = 'www.' + show.title.lower().replace(" ", "") + '.com'
    show1.save()
    return updateshow(request)


def getshow(showname):
    # search by omdb api
    url = "http://www.omdbapi.com/?t=" + showname
    s_detail = json.loads(requests.get(url).text)
    context = {
        'imdbID': s_detail['imdbID'],
        'imdbRating': s_detail['imdbRating'],
        'imdbVotes': s_detail['imdbVotes'],
        'totalSeasons': s_detail['totalSeasons'],
        'Year': s_detail['Year'],
        'Released': s_detail['Released'],
        'Plot': s_detail['Plot'],
        'Link': 'www.imdb.com/title/' + s_detail['imdbID'] + '/',
        'Poster': s_detail['Poster'],
    }
    return context


