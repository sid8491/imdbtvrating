import requests
from django.shortcuts import get_object_or_404, HttpResponse
import json
from show_rating.models import ShowDetail, SeasonDetail, EpisodeDetail
import pandas as pd


def getshowdetails_new(showname):
    s_detail = ShowDetail.objects.get(title=showname)
    episode_dict = EpisodeDetail.objects.filter(showTitle=ShowDetail.objects.get(title=showname)).values()
    episode_dict1 = {}
    episode_dict2 = []
    for obj in episode_dict:
        episode_dict2.append(obj)
    context = {
        'imdbID': s_detail.imdbID,
        'imdbRating': s_detail.imdbRating,
        'imdbVotes': s_detail.imdbVotes,
        'totalSeasons': s_detail.totalSeasons,
        'Year': s_detail.year,
        'Released': s_detail.released,
        'Plot': s_detail.story,
        'Link': 'www.imdb.com/title/' + s_detail.imdbID + '/',
        'Poster': s_detail.poster,
        'episode_dict': episode_dict,
        'episode_dict1': episode_dict1,
        'episode_dict2': episode_dict2,
    }
    return context


def getshowdetails(showname):
    # search by omdb api
    url = "http://www.omdbapi.com/?t=" + showname
    s_detail = json.loads(requests.get(url).text)
    if s_detail['Response'] == "True":
        if s_detail['Type'] == 'series':
            # initialize empty dict with number of season
            season_dict = {k: [] for k in range(1, int(s_detail['totalSeasons']) + 1)}
            episode_dict = []
            for i in range(1, int(s_detail['totalSeasons']) + 1):
                url_season = url + "&Season=" + str(i)
                season_detail = json.loads(requests.get(url_season).text)
                season_dict[i] = season_detail
                for j in season_dict[i]['Episodes']:
                    url_episode = url_season + "&Episode=" + j['Episode']
                    episode_detail = json.loads(requests.get(url_episode).text)
                    episode_detail['Season'] = str(episode_detail['Season']).zfill(2)
                    episode_detail['Episode'] = str(episode_detail['Episode']).zfill(2)
                    episode_dict.append(episode_detail)
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
                'episode_dict': episode_dict,
            }
        else:
            context = {
                'Error': 'Its not a TV Show',
                'Type': s_detail['Type'],
                'imdbID': s_detail['imdbID'],
                'imdbRating': s_detail['imdbRating'],
                'imdbVotes': s_detail['imdbVotes'],
                'Year': s_detail['Year'],
                'Released': s_detail['Released'],
                'Plot': s_detail['Plot'],
                'Link': 'www.imdb.com/title/' + s_detail['imdbID'] + '/',
                'Poster': s_detail['Poster']
            }
    else:
        context = {
            'Response': s_detail['Response'],
            'Error': s_detail['Error'],
        }
    return context


def series_trend(detail):
    x = pd.DataFrame.from_dict(detail)
    x.index += 1
    return x


def updateshowget(showname):
    show_update = get_object_or_404(ShowDetail, title=showname)
    # search by omdb api
    url = "http://www.omdbapi.com/?t=" + showname
    s_detail = json.loads(requests.get(url).text)
    if s_detail['Response'] == "True":
        if s_detail['Type'] == 'series':
            show_update.imdbID = s_detail['imdbID']
            show_update.imdbRating = s_detail['imdbRating']
            show_update.imdbVotes = s_detail['imdbVotes']
            show_update.totalSeasons = s_detail['totalSeasons']
            show_update.year = s_detail['Year']
            show_update.released = s_detail['Released']
            show_update.story = s_detail['Plot']
            show_update.link = 'www.imdb.com/title/' + s_detail['imdbID'] + '/'
            show_update.poster = s_detail['Poster']
            show_update.save()

            # initialize empty dict with number of season
    season_dict = {k: [] for k in range(1, int(s_detail['totalSeasons']) + 1)}
    for i in range(1, int(s_detail['totalSeasons']) + 1):
        url_season = url + "&Season=" + str(i)
        season_detail = json.loads(requests.get(url_season).text)
        season_dict[i] = season_detail
        season_url = "http://www.imdb.com/title/" + s_detail['imdbID'] + "/episodes?season=" + str(i)
        # initialize SeasonDetail table object
        season_update = SeasonDetail()
        # season_update.title, created = ShowDetail.objects.update_or_create(title=showname)
        if SeasonDetail.objects.filter(title=ShowDetail.objects.filter(title=showname), season=str(i).zfill(2)):
            SeasonDetail.objects.filter(title=ShowDetail.objects.get(title=showname),
                                        season=str(i).zfill(2)).update(link=season_url)
        else:
            season_update.title = ShowDetail.objects.get(title=showname)
            season_update.season = str(i).zfill(2)
            season_update.link = season_url
            season_update.save()
        for j in season_dict[i]['Episodes']:
            url_episode = url_season + "&Episode=" + j['Episode']
            episode_detail = json.loads(requests.get(url_episode).text)
            episode_detail['Season'] = str(episode_detail['Season']).zfill(2)
            episode_detail['Episode'] = str(episode_detail['Episode']).zfill(2)
            if EpisodeDetail.objects.filter(showTitle=ShowDetail.objects.filter(title=showname), seasonNumber=
            SeasonDetail.objects.filter(season=str(episode_detail['Season']).zfill(2)), episodeNumber=str(j['Episode']).
                    zfill(2)):
                EpisodeDetail.objects.filter(showTitle=ShowDetail.objects.filter(title=showname),
                                             seasonNumber=SeasonDetail.objects.filter(
                                                 season=str(episode_detail['Season']).zfill(2)),
                                             episodeNumber=str(j['Episode']).zfill(2)).update(
                    episodeTitle=episode_detail['Title'],
                    episodeNumber=str(episode_detail['Episode']).zfill(2),
                    rating=episode_detail['imdbRating'],
                    raters=episode_detail['imdbVotes'],
                    synopsis=episode_detail['Plot'],
                    airdate=episode_detail['Released'],
                    link='www.imdb.com/title/' + episode_detail['imdbID'] + '/',
                    imdbID=episode_detail['imdbID'],
                    runTime=episode_detail['Runtime'],
                    genre=episode_detail['Genre'],
                    director=episode_detail['Director'],
                    seasonNumber1=str(i).zfill(2),
                    showTitle1=showname,)
            else:
                # initialize SeasonDetail table object
                episode_update = EpisodeDetail()
                episode_update.showTitle = ShowDetail.objects.get(title=showname)
                episode_update.showTitle1 = showname
                episode_update.seasonNumber = SeasonDetail.objects.filter(season=str(i).zfill(2))[0]
                episode_update.seasonNumber1 = str(i).zfill(2)
                episode_update.episodeTitle = episode_detail['Title']
                episode_update.episodeNumber = str(episode_detail['Episode']).zfill(2)
                episode_update.rating = episode_detail['imdbRating']
                episode_update.raters = episode_detail['imdbVotes']
                episode_update.synopsis = episode_detail['Plot']
                episode_update.airdate = episode_detail['Released']
                episode_update.link = 'www.imdb.com/title/' + episode_detail['imdbID'] + '/'
                episode_update.imdbID = episode_detail['imdbID']
                episode_update.runTime = episode_detail['Runtime']
                episode_update.genre = episode_detail['Genre']
                episode_update.director = episode_detail['Director']
                episode_update.save()
