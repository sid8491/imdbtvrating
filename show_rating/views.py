from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.admin.views.decorators import staff_member_required
from .models import ShowDetail
from show_rating.logic import showdetails as sd
import string


def show(request):
    context = {'all_shows': ShowDetail.objects.all()}
    return render(request, 'show_rating/show.html', context)


def show_detail(request, show_name):
    try:
        # checkfromdb = ShowDetail.objects.get(title=show_name)
        show_name = string.capwords(show_name)
        detail = sd.getshowdetails(show_name)
        if 'Error' not in detail:
            context = {
                'detail': detail,
                'title': show_name,
            }
            return render(request, 'show_rating/details.html', context)
        else:
            if 'Type' in detail:
                context = {
                    'detail': detail,
                    'title': show_name,
                }
                return render(request, 'show_rating/details.html', context)
            else:
                raise Http404(detail['Error'])
    except ShowDetail.DoesNotExist:
        raise Http404(detail['Error'])


def updateshow(request):
    context = {'all_details': ShowDetail.objects.all()}
    return render(request, 'some.html', context)


updateshow = staff_member_required(updateshow)


def updateshowget(request):
    try:
        show1 = get_object_or_404(ShowDetail, title=request.POST['Show'])
    except Exception as e:
        print(e)
    context = sd.getshowdetails(str(show1))
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




