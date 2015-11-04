from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.shortcuts import render, redirect
from datetime import datetime

from django.contrib import messages

from .models import Child, DailyReport
from .forms import ChildForm, DailyReportForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    '''
    returns current time in html
    '''
    now = datetime.now()
    html = "<html><body>Hello world. It is now {} local server time.</body></html>".format(
        now)
    return HttpResponse(html)


class ChildActionMixin(object):
    fields = ('first_name', 'gender', 'birthday',
              'parent_name', 'parent_email', 'parent_phone')

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(ChildActionMixin, self).form_valid(form)


class ChildListView(ListView):

    model = Child
    template_name = 'careapp/childs_list.html'


class ChildCreateView(ChildActionMixin, CreateView):

    model = Child
    # fields = ('first_name', 'gender', 'birthday',
    #           'parent_name', 'parent_email', 'parent_phone')
    #
    template_name = 'careapp/edit_child.html'
    success_msg = "Child created!"

    def get_success_url(self):
        return reverse('childs-list')


class ChildUpdateView(ChildActionMixin, UpdateView):
    model = Child
    # fields = ('first_name', 'gender', 'birthday',
    #           'parent_name', 'parent_email', 'parent_phone')

    success_msg = "Child updated!"


class ChildDetailView(DetailView):
    model = Child


# @login_required
def add_child(request):
    if request.method == 'POST':
        form = ChildForm(request.POST)
        if form.is_valid():
            child = form.save(commit=False)
            child.save()
            messages.add_message(request, messages.SUCCESS, 'Child added.')
            return redirect('children-list')
        else:
            messages.add_message(request, messages.ERROR, 'Form data invalid.')

    else:
        form = ChildForm()
    return render(request, 'careapp/edit_child.html',
                  {'form': form})


# class DailyReportCreateView(CreateView):
#
#     model = DailyReport
#     template_name = 'careapp/daily_report.html'
#     fields = ('date', 'child', 'arrival_time',
#               'departure_time', 'mood_am', 'mood_pm')


class DailyReportMixin(object):
    fields = ('date', 'child', 'arrival_time',
              'departure_time', 'mood_am', 'mood_pm')
    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(DailyReportMixin, self).form_valid(form)

class DailyReportCreateView(DailyReportMixin, CreateView):
    model = DailyReport
    template_name = 'careapp/daily_report.html'
    success_msg = "Initial Daily Report saved"

# @login_required
    def daily_report(request):
        '''

        Opens the Daily sign-in form.
        '''
        if request.method == 'POST':
            form = DailyReportForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('daily-report')
        else:
            form = DailyReportCreateView()
        return render(request, 'daily_report.html',
                      {'form': form})

    def get_success_url(self):
        return reverse('daily-report')


class DailyReportUpdateView(DailyReportMixin, UpdateView):
    model = DailyReport
    success_msg = "Daily Report Updated"


class DailyReportDetailView(DailyReportMixin, DetailView):
    model = DailyReport
