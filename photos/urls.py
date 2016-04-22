# photos/urls.py
from django.conf.urls import url

from . import views


app_name = 'photos'

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/like/$', views.like_photo, name='like_photo'),
    url(r'^(?P<pk>[0-9]+)/$', views.view_photo, name='view_photo'),
    url(r'^$', views.toppage, name='toppage'),
]
