from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show, name='show'),
    url(r'^(?P<show_name>[%&+ \w]+)/$', views.show_detail, name='show_detail'),
]

