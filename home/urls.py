from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^hire-me/$', views.hireme, name='hireme'),
    url(r'^hiremesubmit/$', views.hiremesubmit, name='hiremesubmit'),
    url(r'^suggestions/$', views.suggestions, name='suggestions'),
    url(r'^suggestionssubmit/$', views.suggestionssubmit, name='suggestionssubmit'),
    url(r'^contact-us/$', views.contactus, name='contactus')
]