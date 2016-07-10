from django.db import models


class ShowDetail(models.Model):
    title = models.CharField(max_length=100)
    imdb_id = models.CharField(max_length=20, null=True, blank=True)
    rating = models.CharField(max_length=10, null=True, blank=True)
    raters = models.CharField(max_length=10, null=True, blank=True)
    total_seasons = models.CharField(max_length=5, null=True, blank=True)
    year = models.CharField(max_length=20, null=True, blank=True)
    release = models.CharField(max_length=20, null=True, blank=True)
    story = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=200, null=True, blank=True)
    poster = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title


class SeasonDetail(models.Model):
    show_title = models.ForeignKey(ShowDetail, on_delete=models.CASCADE)
    season = models.CharField(max_length=5, null=True, blank=True)
    total_episodes = models.CharField(max_length=5, null=True, blank=True)
    link = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "Season " + str(self.season)


class EpisodeDetail(models.Model):
    show_title = models.ForeignKey(SeasonDetail, on_delete=models.CASCADE)
    episode_title = models.CharField(max_length=100, null=True, blank=True)
    season = models.CharField(max_length=5, null=True, blank=True)
    episode = models.CharField(max_length=5, null=True, blank=True)
    episode_name = models.CharField(max_length=100, null=True, blank=True)
    rating = models.CharField(max_length=10, null=True, blank=True)
    raters = models.CharField(max_length=10, null=True, blank=True)
    synopsis = models.TextField(null=True, blank=True)
    airdate = models.CharField(max_length=100, null=True, blank=True)
    link = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "Episode " + str(self.episode)