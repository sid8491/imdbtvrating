import requests
import json


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


# for show details page, called from views->show_detail
def getshowdetails(showname):
    context = getshow(showname)
    return context