import requests
import json


def getshowdetails(showname):
    # search by omdb api
    url = "http://www.omdbapi.com/?t=" + showname
    s_detail = json.loads(requests.get(url).text)
    if 'Error' not in s_detail:
        if s_detail['Type'] == 'series':
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


    # for show details page, called from views->show_detail
    # def getshowdetails(showname):
    # context = getshow(showname)
    # return context