from django.contrib import admin
from .models import HireMe, Suggestion
# Register your models here.


class HireMeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number', 'comments', 'submit_date')
    list_filter = ('submit_date',)


class SuggestionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'suggestion', 'submit_date')
    list_filter = ('submit_date',)


admin.site.register(HireMe, HireMeAdmin)
admin.site.register(Suggestion, SuggestionAdmin)
