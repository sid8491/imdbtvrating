from django.db import models


class ShowDetail(models.Model):
    title = models.CharField(max_length=100)
    imdbID = models.CharField(max_length=20, null=True, blank=True)
    imdbRating = models.CharField(max_length=10, null=True, blank=True)
    imdbVotes = models.CharField(max_length=10, null=True, blank=True)
    totalSeasons = models.CharField(max_length=5, null=True, blank=True)
    year = models.CharField(max_length=20, null=True, blank=True)
    released = models.CharField(max_length=20, null=True, blank=True)
    story = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=200, null=True, blank=True)
    poster = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title


class SeasonDetail(models.Model):
    title = models.ForeignKey(ShowDetail, on_delete=models.CASCADE)
    season = models.CharField(max_length=5, null=True, blank=True)
    totalEpisodes = models.CharField(max_length=5, null=True, blank=True)
    link = models.CharField(max_length=200, null=True, blank=True)
    imdbID = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.season


class EpisodeDetail(models.Model):
    showTitle = models.ForeignKey(ShowDetail, on_delete=models.CASCADE)
    showTitle1 = models.CharField(max_length=100, null=True, blank=True)
    seasonNumber = models.ForeignKey(SeasonDetail, on_delete=models.CASCADE)
    seasonNumber1 = models.CharField(max_length=5, null=True, blank=True)
    episodeTitle = models.CharField(max_length=100, null=True, blank=True)
    episodeNumber = models.CharField(max_length=5, null=True, blank=True)
    rating = models.CharField(max_length=10, null=True, blank=True)
    raters = models.CharField(max_length=10, null=True, blank=True)
    synopsis = models.TextField(null=True, blank=True)
    airdate = models.CharField(max_length=100, null=True, blank=True)
    link = models.CharField(max_length=200, null=True, blank=True)
    imdbID = models.CharField(max_length=20, null=True, blank=True)
    runTime = models.CharField(max_length=20, null=True, blank=True)
    genre = models.CharField(max_length=100, null=True, blank=True)
    director = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.episodeNumber).zfill(2)


class AbsentShow(models.Model):
    absentTitle = models.CharField(max_length=1000)

    def __str__(self):
        return self.absentTitle