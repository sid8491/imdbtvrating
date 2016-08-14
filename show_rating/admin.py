from django.contrib import admin
from .models import ShowDetail, SeasonDetail, EpisodeDetail, AbsentShow


class EpisodeDetailAdmin(admin.ModelAdmin):
    list_display = ('showTitle', 'seasonNumber', 'episodeNumber', 'rating', 'airdate')
    list_filter = ('showTitle', 'seasonNumber')


class SeasonDetailAdmin(admin.ModelAdmin):
    list_display = ('title', 'season', 'link')
    list_filter = ('title', 'season')


admin.site.register(ShowDetail)
admin.site.register(SeasonDetail, SeasonDetailAdmin)
admin.site.register(EpisodeDetail, EpisodeDetailAdmin)
admin.site.register(AbsentShow)
