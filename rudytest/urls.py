from django.conf.urls import patterns, include, url
from django.contrib import admin
from app.serializers import *

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/messages/$', MessageList.as_view(), name='messages-list'),
    url(r'^api/messages/(?P<pk>[0-9]+)/$', MessageDetail.as_view(), name='messages-detail'),
    url(r'^api/chatters/$', MessageList.as_view(), name='chatters-list'),
    url(r'^api/chatters/(?P<pk>[0-9]+)/$', MessageDetail.as_view(), name='chatters-detail'),
)
