from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.contrib.admin.views.decorators import staff_member_required
from .models import ShowDetail
from show_rating.logic import showdetails as sd
import string
from plotly.offline import plot
from plotly.graph_objs import *


def show(request):
    context = {'all_shows': ShowDetail.objects.all()}
    return render(request, 'show_rating/show.html', context)


def show_detail(request, show_name):
    try:
        # checkfromdb = ShowDetail.objects.get(title=show_name)
        show_name = string.capwords(show_name)
        detail = sd.getshowdetails(show_name)
        if 'Error' not in detail:
            series_trend = sd.series_trend(detail['episode_dict'])
            scatterplot = plot([Scatter(
            x=series_trend.index,
            y=series_trend['imdbRating'],
                mode='markers', marker=dict(size=10,
                                            color=series_trend['Season'],
                                            colorscale='Viridis', showscale=True),
                text=('S' + series_trend['Season'] + 'E' + series_trend['Episode'] + '<br>' + series_trend['Title']))],
                output_type='div')
            barplot = plot([Bar(
                x=series_trend['Season'],
                y=series_trend['imdbRating'], text=(series_trend['imdbRating']))],
                output_type='div')
            # scatterplot = plot(Figure(data=Data([
            #     Scatter(
            #         x=series_trend.index,
            #         y=series_trend['imdbRating'],
            #         mode='markers', marker=dict(size=10,
            #                                     color=series_trend['Season'],
            #                                     colorscale='Viridis', showscale=True),
            #         text=('S' + series_trend['Season'] + 'E' + series_trend['Episode'] + '<br>' + series_trend['Title']))],
            #     layout=Layout(
            #         title='My tite',
            #         # paper_bgcolor='rgba(12,150,30,10)',
            #         plot_bgcolor='rgb(158,36,156)'
            #     ))), output_type='div')
            # barplot = plot([Bar(
            #     x=series_trend['Season'],
            #     y=series_trend['imdbRating'], text=(series_trend['imdbRating']))],
            #     output_type='div')
            context = {
                'detail': detail,
                'title': show_name,
                'div_scatterplot': scatterplot,
                'div_barplot': barplot,
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
    show1 = get_object_or_404(ShowDetail, title=request.POST['Show'])
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


def search_show(request):
    # return show_detail(request, request.GET['q'])
    return HttpResponseRedirect(reverse('show_detail', kwargs={'show_name': request.GET['q']}))
