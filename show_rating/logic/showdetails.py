import requests
import json
import pandas as pd


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



