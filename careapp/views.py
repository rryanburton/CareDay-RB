from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.shortcuts import render, redirect
from datetime import datetime, date
# from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Child, DailyReport, Diapering, Sleeping, Eating
from .forms import ChildForm, DailyReportForm
# , DiaperingFormSet, SleepingFormSet, EatingFormSet
# from extra_views import UpdateWithInlinesView, InlineFormSet
# from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django import forms


# Create your views here.

###############################################################################
#   Index

def index(request):
    '''
    returns current time in html
    '''
    now = datetime.now()
    html = "<html><body>Welcome to CareDay! <br> The current time is: {} local server time.</body></html>".format(
            now)
    return HttpResponse(html)


###############################################################################
#   Child


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
    template_name = 'careapp/childs_list2.html'


class BobChildListView(ListView):
    model = Child
    template_name = 'careapp/bobchild_list.html'


class BobChildDeleteView(ChildActionMixin, DeleteView):
    model = Child
    success_url = reverse_lazy('bob-child')  # re-directs user here.
    template_name = 'careapp/bobdelete_child.html'

    # def get_object(self, queryset=None):
    #     obj = Child.objects.get(id=self.kwargs['id'])
    #     obj.delete()
    #     return HttpResponse("Deleted Child")

    # def delete(request):
    #     query = Child.objects.get(pk=id)
    #     query.delete()
    #     return HttpResponse("Deleted Child!")


class ChildCreateView(ChildActionMixin, CreateView):
    model = Child
    template_name = 'careapp/edit_child.html'
    success_msg = "Child created!"

    def get_success_url(self):
        return reverse('childs-list')


class ChildUpdateView(ChildActionMixin, UpdateView):
    model = Child
    template_name_suffix = '_update_form'
    success_msg = "Child updated!"

    def get(self, request, **kwargs):
        self.object = Child.objects.get(id=self.kwargs['id'])
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def get_object(self, queryset=None):
        obj = Child.objects.get(id=self.kwargs['id'])
        return obj

    def get_success_url(self):
        return reverse('childs-list')


class ChildDetailView(DetailView):
    model = Child


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


###############################################################################
#  DAILY REPORT PANELS


class DailyReportActionMixin(object):
    fields = ( 'arrival_time',
              'departure_time', 'mood_am', 'mood_pm')

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(DailyReportActionMixin, self).form_valid(form)


class DailyReportListView(ListView):
    model = DailyReport
    template_name = 'careapp/daily_report_list.html'

    # template_name_suffix = '_list'

    def get_queryset(self):
        filterdate = '2015-11-10'
        preload = DailyReport.objects.all().select_related('child')
        return preload.filter(date=filterdate).order_by('arrival_time')
        # return preload.order_by('-date')


class DailyReportCreateView(DailyReportActionMixin, CreateView):
    model = DailyReport
    template_name = 'careapp/daily_report_initial.html'
    success_msg = "Daily Report created"

    def daily_report(request):
        '''
        Opens the Daily sign-in form.
        '''
        if request.method == 'POST':
            form = DailyReportForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('dailyreport-new')
        else:
            form = DailyReportCreateView()
        return render(request, 'careapp/daily_report.html',
                      {'form': form})

    def get_success_url(self):
        return reverse('childs-list')


class DailyReportUpdateView(UpdateView):
    fields = ('arrival_time',
              'departure_time', 'mood_am', 'mood_pm')

    model = DailyReport
    form = DailyReportForm
    form_name = DailyReportForm
    template_name = 'careapp/daily_report.html'
    success_msg = "Daily Report updated!"

    DiaperingFormSet = inlineformset_factory(DailyReport, Diapering,
                                                 fields=('time_diaper', 'num_one', 'num_two', 'comments'),
                                                 widgets={
                                                    'time_diaper': forms.TimeInput(attrs={'class': 'time_diaper'}),
                                                    # 'time_diaper': forms.TimeField(widget=TimeWidget(usel10n=True, bootstrap_version=3)),
                                                 },
                                                 labels={
                                                    'time_diaper': 'Potty time',
                                                    'num_one': 'Wet',
                                                    'num_two': 'BM',
                                                 },
                                                 extra=1
                                                 )

    SleepingFormSet = inlineformset_factory(DailyReport, Sleeping,
                                            fields=('time_slp_start', 'time_slp_end'),
                                            widgets={
                                                'time_slp_start': forms.TimeInput(attrs={'class': 'time_slp_start'}),
                                                'time_slp_end': forms.TimeInput(attrs={'class': 'time_slp_end'}),
                                             },
                                            labels={
                                                'time_slp_start': 'Nap time start',
                                                'time_slp_end': 'Nap time finish',

                                             },
                                            extra=1)

    EatingFormSet = inlineformset_factory(DailyReport, Eating,
                                             fields=('time_eat', 'food', 'leftover'),
                                             widgets={
                                                'time_eat': forms.TimeInput(attrs={'class': 'time_slp_start'}),
                                             },
                                             labels={
                                                'time_eat': 'Meal time',
                                             },
                                             extra=1)

    # inlines = [DiaperingFormSet, SleepingFormSet, EatingFormSet]
    # inlines = [DiaperingFormSet]
    # template_name_suffix = '_update_form'

    #
    # def get(self, request, **kwargs):
    #     self.object, created = DailyReport.objects.get_or_create(
    #         child_id=self.kwargs['child_id'],
    #         date=date.today(), )
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     context = self.get_context_data(object=self.object, form=form)
    #     return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(DailyReportUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['diapering_formset'] = self.DiaperingFormSet(self.request.POST, instance=context['object'])
            context['sleeping_formset'] = self.SleepingFormSet(self.request.POST, instance=context['object'])
            context['eating_formset'] = self.EatingFormSet(self.request.POST, instance=context['object'])
        else:
            context['diapering_formset'] = self.DiaperingFormSet(instance=context['object'])
            context['sleeping_formset'] = self.SleepingFormSet(instance=context['object'])
            context['eating_formset'] = self.EatingFormSet(instance=context['object'])
        return context

    def post(self, request, *args, **kwargs):
            """
            Handles POST requests, instantiating a form instance and its inline
            formsets with the passed POST variables and then checking them for
            validity.
            """
            self.object = None
            form_name = self.get_form_class()
            form = self.get_form(form_name)
            diapering_form = self.DiaperingFormSet(self.request.POST)
            sleeping_form = self.SleepingFormSet(self.request.POST)
            eating_form = self.EatingFormSet(self.request.POST)
            if (form.is_valid() and diapering_form.is_valid() and
                sleeping_form.is_valid() and eating_form.is_valid()):
                return self.form_valid(form, diapering_form, sleeping_form, eating_form)
            else:
                return self.form_invalid(form, diapering_form, sleeping_form, eating_form)

    def form_valid(self, form, diapering_form, sleeping_form, eating_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        diapering_form.instance = self.object
        diapering_form.save()
        sleeping_form.instance = self.object
        sleeping_form.save()
        eating_form.instance = self.object
        eating_form.save()
        return HttpResponseRedirect(self.get_success_url())

    # def form_valid(self, form):
    #     messages.info(self.request, self.success_msg)
    #     return super().form_valid(form)

    def form_invalid(self, form, diapering_form, sleeping_form, eating_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  diapering_form=diapering_form,
                                  sleeping_form=sleeping_form,
                                  eating_form=eating_form,
                                  ))

    def get_object(self, queryset=None):
        obj, created = DailyReport.objects.get_or_create(child_id=self.kwargs['child_id'],
            date=date.today(), )
        return obj

    def get_success_url(self):
        return reverse('childs-list')


class DailyReportDetailView(DailyReportActionMixin, DetailView):
    model = DailyReport


###############################################################################
# DIAPERING TABLES


class DiaperingMixin(object):
    fields = ('dailyreport', 'time_diaper', 'num_one',
              'num_two', 'comments')

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(DiaperingMixin, self).form_valid(form)


class DiaperingCreateView(DiaperingMixin, CreateView):
    model = Diapering
    #    template_name = 'careapp/edit_child.html'
    success_msg = "Diapering completed"

    # def get_success_url(self):
    #     return reverse('childs-list')

    def diapering(request):

        if request.method == 'POST':
            form = DiaperingForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('diapering')
        else:
            form = DiaperingCreateView()
        return render(request, 'careapp/diapering_form.html',
                      {'form': form})

    def get_success_url(self):
        return reverse('diapering')


class DiaperingUpdateView(DiaperingMixin, UpdateView):
    model = Diapering
    success_msg = "Diapering completed"


class DiaperingDetailView(DiaperingMixin, DetailView):
    model = Diapering


###############################################################################
# SLEEPING TABLES


class SleepingMixin(object):
    fields = ('dailyreport', 'time_slp_start', 'time_slp_end')

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(SleepingMixin, self).form_valid(form)


class SleepingCreateView(SleepingMixin, CreateView):
    model = Sleeping
    success_msg = "Sleeping recorded"

    def sleeping(request):
        '''
        Opens the Sleeping activity panel.
        '''
        if request.method == 'POST':
            form = SleepingForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('sleeping')
        else:
            form = SleepingCreateView()
        return render(request, 'sleeping_form.html',
                      {'form': form})

    def get_success_url(self):
        return reverse('sleeping')


class SleepingUpdateView(SleepingMixin, UpdateView):
    model = Sleeping
    success_msg = "Sleeping recorded"


class SleepingDetailView(SleepingMixin, DetailView):
    model = Sleeping


###############################################################################
#  EATING TABLES


class EatingMixin(object):
    fields = ('dailyreport', 'time_eat', 'food', 'leftover')

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(EatingMixin, self).form_valid(form)


class EatingCreateView(EatingMixin, CreateView):
    model = Eating
    success_msg = "Food Intake recorded"

    def sleeping(request):
        '''
        Opens the Eating activity panel.
        '''
        if request.method == 'POST':
            form = EatingForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('eating')
        else:
            form = EatingCreateView()
        return render(request, 'eating_form.html',
                      {'form': form})

    def get_success_url(self):
        return reverse('eating')


class EatingUpdateView(EatingMixin, UpdateView):
    model = Eating
    success_msg = "Food Intake recorded"


class EatingDetailView(EatingMixin, DetailView):
    model = Eating


###############################################################################

class TerryCreateView(CreateView):

    model = DailyReport
    template_name = 'careapp/daily_report.html'
    fields = ('date', 'child', 'arrival_time',
              'departure_time', 'mood_am', 'mood_pm')


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

###############################################################################
#  ARCHIVE VIEWS

class ArchiveDateDailyReportListView(ListView):
    model = DailyReport
    template_name = 'careapp/archive_date.html'


    def get_queryset(self):
        filterdate = '2015-11-13'
        preload = DailyReport.objects.all().select_related('child')
        return preload
        # return preload.filter(date=filterdate).order_by('arrival_time')
        # return preload.order_by('-date')

class ArchiveChildDailyReportListView(ListView):
    model = DailyReport
    template_name = 'careapp/archive_child.html'


    def get_queryset(self):
        filterdate = '2015-11-10'
        preload = DailyReport.objects.all().select_related('child')
        return preload.filter(child_id='4').order_by('-date')
        # return preload.order_by('-date')

###############################################################################
