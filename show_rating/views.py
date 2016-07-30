from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.contrib.admin.views.decorators import staff_member_required
from .models import ShowDetail
from show_rating.logic import showdetails as sd
import string
from plotly.offline import plot
from plotly.graph_objs import *
from django.views.decorators.cache import never_cache


def show(request):
    context = {'all_shows': ShowDetail.objects.all().order_by('title')}
    return render(request, 'show_rating/show.html', context)


def show_detail(request, show_name):
    try:
        # checkfromdb = ShowDetail.objects.get(title=show_name)
        show_name = string.capwords(show_name)
        detail = sd.getshowdetails(show_name)
        if 'Error' not in detail:
            series_trend = sd.series_trend(detail['episode_dict'])
            layout = dict(
                title=show_name,
                titlefont=dict(
                    family='Calibri, sans-serif',
                    size=36,
                ),
                yaxis=dict(
                    title='Rating',
                    titlefont=dict(
                        family='Arial, sans-serif',
                        size=18,
                    ),
                    autorange=True,
                ),
                xaxis=dict(
                    title='Episodes',
                    titlefont=dict(
                        family='Arial, sans-serif',
                        size=18,
                    ),
                    autorange=True,
                ),
                plot_bgcolor='rgba(238, 238, 238, 1.0)',
                paper_bgcolor='rgba(238, 238, 238, 1.0)',
            )
            data = Data([
                Scatter(
                    x=series_trend.index,
                    y=series_trend['imdbRating'],
                    mode='markers', marker=dict(size=10,
                                                color=series_trend['Season'],
                                                colorscale='Viridis', showscale=True),
                    text=(
                        'S' + series_trend['Season'] + 'E' + series_trend['Episode'] + '<br>' + series_trend['Title']))
            ])
            fig = Figure(data=data, layout=layout)
            scatterplot = plot(fig, output_type='div')

            layout_bar = dict(
                yaxis=dict(
                    title='Average Rating',
                    titlefont=dict(
                        family='Arial, sans-serif',
                        size=18,
                    ),
                    autorange=True,
                ),
                xaxis=dict(
                    title='Seasons',
                    titlefont=dict(
                        family='Arial, sans-serif',
                        size=18,
                    ),
                    autorange=True,
                ),
                plot_bgcolor='rgba(238, 238, 238, 1.0)',
                paper_bgcolor='rgba(238, 238, 238, 1.0)',
            )
            data_bar = Data([
                Bar(
                    x=series_trend['Season'],
                    y=series_trend['imdbRating'],
                    marker=dict(color=series_trend['Season'],
                                colorscale='Viridis', showscale=False),
                    hoverinfo='none',
                ),
            ])
            fig_bar = Figure(data=data_bar, layout=layout_bar)
            barplot = plot(fig_bar, output_type='div')

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
    show1.save()
    return updateshow(request)


def search_show(request):
    return HttpResponseRedirect(reverse('show_detail', kwargs={'show_name': request.GET['q']}))


@never_cache
def page_not_found(request):
    return render(request, 'show_rating/404.html')