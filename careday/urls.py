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
<<<<<<< HEAD
from careapp.views import index, ChildListView, ChildCreateView, ChildUpdateView, DailyReportCreateView
from careapp.views import add_child, DailyReportUpdateView, DailyReportDetailView
=======
from django.views.generic import TemplateView
from careapp.views import ChildListView, ChildCreateView, ChildUpdateView, DailyReportCreateView, add_child
>>>>>>> 6119805f54932e9bfb6dcb22a945f4ef91aeb11c


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^child$', ChildListView.as_view(), name='childs-list',),
    url(r'^child/new$', ChildCreateView.as_view(), name='child-new',),
    url(r'^dailyintake$', DailyReportCreateView.as_view(),
        name='daily-report',),
<<<<<<< HEAD
    url(r'^child/update/(?P<id>\d+)/$', ChildUpdateView.as_view(), name='child-update'),
    url(r'^dailyintake/update/(?P<id>\d+)/$', DailyReportUpdateView.as_view(), name='daily-update'),
    url(r'^dailyintake/detail/(?P<id>\d+)/$', DailyReportDetailView.as_view(), name='daily-detail'),
    url(r'^$', index, name='index'),
=======
    url(r'^child/update/(?P<id>\d+)/$',
        ChildUpdateView.as_view(), name='child-update'),
    url(r'^$', TemplateView.as_view(
        template_name='careapp/index.html'), name='index',),
    # url(r'^$', index, name='index'),
>>>>>>> 6119805f54932e9bfb6dcb22a945f4ef91aeb11c
]
