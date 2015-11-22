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
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from careapp.views import ChildListView, ChildCreateView, ChildUpdateView, \
    DailyReportListView, DailyReportCreateView, DailyReportUpdateView, \
    add_child, DiaperingCreateView, SleepingCreateView, EatingCreateView, \
    ArchiveChildDailyReportListView, ArchiveDateDailyReportListView, \
    TerryCreateView, ChildMgtListView, ChildMgtDeleteView

from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^$', TemplateView.as_view(
        template_name='careapp/index.html'), name='index',),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'},
        name='careday_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': reverse_lazy('index')},
        name='careday_logout'),
    url(r'^child$', ChildListView.as_view(), name='childs-list', ),
    url(r'^child/update/(?P<pk>\d+)/$',
        ChildUpdateView.as_view(), name='child-update'),
    url(r'^child/new$', ChildCreateView.as_view(), name='child-new', ),
    url(r'^dailyreport$', DailyReportListView.as_view(),
        name='dailyreport-list', ),
    url(r'^dailyreport/new$', DailyReportCreateView.as_view(),
        name='dailyreport-new', ),
    # # url(r'^dailyreport/update/(?P<id>\d+)/$',
    #     DailyReportUpdateView.as_view(), name='dailyreport-update'),


    url(r'^dailyreport/update/(?P<child_id>\d+)/$',
        DailyReportUpdateView.as_view(), name='dailyreport-update'),
    # url(r'^dailyreport/detail/(?P<pk>\d+)/$',
    #     DailyReportDetailView.as_view(), name='dailyreport-detail'),

    url(r'^dailyreport/(?P<date>\d{4}-\d{2}-\d{2})/(?P<child_id>\d+)/$',
        DailyReportUpdateView.as_view(),  name='dailyreport-update-date'),


    # url(r'^$', index, name='index'),
    # url(r'^calendar$', TemplateView.as_view(
    #     template_name='careapp/calendar.html'), name='calendar', ),
    # url(r'^diapering/new$', DiaperingCreateView.as_view(), name='diapering', ),
    # url(r'^sleeping/new$', SleepingCreateView.as_view(), name='sleeping', ),
    # url(r'^eating/new$', EatingCreateView.as_view(), name='eating', ),
    # url(r'^dailyintake$', TerryCreateView.as_view(),
    #     name='daily-report', ),

    url(r'^$', TemplateView.as_view(
        template_name='careapp/index.html'), name='index',),
    url(r'^childmgt$', ChildMgtListView.as_view(),
        name='childmgt', ),
    url(r'^childdelete/(?P<pk>\d+)/$', ChildMgtDeleteView.as_view(),
        name='childdelete', ),

    url(r'^archive/date$', ArchiveDateDailyReportListView.as_view(),
        name='archive-list-date', ),
    url(r'^archive/child$', ArchiveChildDailyReportListView.as_view(),
        name='archive-list-child', ),
    # url(r'^archive/bobdate$', BobArchiveDateDailyReportListView.as_view(),
    #     name='archive-list-bobchild', ),

]
