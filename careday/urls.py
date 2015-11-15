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
    TerryCreateView, BobChildListView, BobChildDeleteView, \
    BobDailyReportListView
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'},
        name='careday_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': reverse_lazy('index')},
        name='careday_logout'),
    url(r'^child$', ChildListView.as_view(), name='childs-list', ),
    url(r'^child/new$', ChildCreateView.as_view(), name='child-new', ),
    url(r'^child/update/(?P<id>\d+)/$',
        ChildUpdateView.as_view(), name='child-update'),
    url(r'^dailyreport$', DailyReportListView.as_view(),
        name='dailyreport-list', ),
    url(r'^dailyreport/new$', DailyReportCreateView.as_view(),
        name='dailyreport-new', ),
    # url(r'^dailyreport/update/(?P<id>\d+)/$',
    #     DailyReportUpdateView.as_view(), name='dailyreport-update'),

    # url(r'^dailyreport/update/(?P<date>\d+)/(?P<child_id>\d+)/$',
    #         DailyReportUpdateView.as_view(),  name='dailyreport-update'),

    url(r'^dailyreport/update/(?P<child_id>\d+)/$',
        DailyReportUpdateView.as_view(), name='dailyreport-update'),

    # url(r'^$', index, name='index'),
    url(r'^calander$', TemplateView.as_view(
        template_name='careapp/calander.html'), name='calander', ),
    url(r'^diapering/new$', DiaperingCreateView.as_view(), name='diapering', ),
    url(r'^sleeping/new$', SleepingCreateView.as_view(), name='sleeping', ),
    url(r'^eating/new$', EatingCreateView.as_view(), name='eating', ),
    url(r'^dailyintake$', TerryCreateView.as_view(),
        name='daily-report', ),
    url(r'^$', TemplateView.as_view(
        template_name='careapp/index.html'), name='index',),
    url(r'^bobchild$', BobChildListView.as_view(),
        name='bob-child', ),
    url(r'^bobchilddelete/(?P<pk>\d+)/$', BobChildDeleteView.as_view(),
        name='bob-child-delete', ),
    url(r'^bobdailyreport$', BobDailyReportListView.as_view(),
        name='bobdailyreport-list', ),

]
