"""careday URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from careapp.views import index, ChildListView, ChildCreateView, ChildUpdateView, DailyReportCreateView
from careapp.views import add_child, DailyReportUpdateView, DailyReportDetailView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^child$', ChildListView.as_view(), name='childs-list',),
    url(r'^child/new$', ChildCreateView.as_view(), name='child-new',),
    # url(r'^child/new$', add_child, name='child_new'),
    # url(r'^kids$', ChildListView.as_view(), name='children-list',),
    url(r'^dailyintake$', DailyReportCreateView.as_view(),
        name='daily-report',),
    url(r'^child/update/(?P<id>\d+)/$', ChildUpdateView.as_view(), name='child-update'),
    url(r'^dailyintake/update/(?P<id>\d+)/$', DailyReportUpdateView.as_view(), name='daily-update'),
    url(r'^dailyintake/detail/(?P<id>\d+)/$', DailyReportDetailView.as_view(), name='daily-detail'),
    url(r'^$', index, name='index'),
]
