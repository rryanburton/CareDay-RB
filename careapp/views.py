from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .models import Child, DailyReport, Diapering, Sleeping, Eating
from .forms import ChildForm, DailyReportForm, DiaperingForm, \
     SleepingForm, EatingForm, DiaperingFormSet
from django.contrib.auth.decorators import login_required
# Create your views here.


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
    template_name = 'careapp/childs_list.html'


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
    fields = ('date', 'child', 'arrival_time',
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
        preload = DailyReport.objects.all().select_related('child')
        return preload.order_by('-date')


# class DailyReportCreateView(DailyReportActionMixin, CreateView):
#
#     model = DailyReport
#     template_name = 'careapp/daily_report_initial.html'
#     success_msg = "Daily Report created"
#
#     def daily_report(request):
#         '''
#         Opens the Daily sign-in form.
#         '''
#         if request.method == 'POST':
#             form = DailyReportForm(request.POST)
#             if form.is_valid():
#                 form.save()
#             return redirect('dailyreport-new')
#         else:
#             form = DailyReportCreateView()
#         return render(request, 'daily_report.html',
#                       {'form': form})
#
#     def get_success_url(self):
#         return reverse('dailyreport-list')

        ''' ######## - Inline Form Replacement - ########'''


class DailyReportCreateView(CreateView):
    # template_name = 'dailyreport_add.html'
    model = DailyReport
    form_class = DailyReportForm
    fields = ('date', 'child', 'arrival_time',
              'departure_time', 'mood_am', 'mood_pm')
#    success_url = 'success/'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        diapering_form = DiaperingFormSet()
#        instruction_form = InstructionFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  diapering_form=diapering_form,))
#                                  instruction_form=instruction_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        diapering_form = DiaperingFormSet(self.request.POST)
#        instruction_form = InstructionFormSet(self.request.POST)
        if (form.is_valid() and diapering_form.is_valid()):
            # and
            # instruction_form.is_valid()
            # ):
            return self.form_valid(form, diapering_form)
        else:
            return self.form_invalid(form, diapering_form)

    def form_valid(self, form, diapering_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        diapering_form.instance = self.object
        diapering_form.save()
        # instruction_form.instance = self.object
        # instruction_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, diapering_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  diapering_form=diapering_form,))
#                                  instruction_form=instruction_form))


class DailyReportUpdateView(DailyReportActionMixin, UpdateView):

    model = DailyReport
    template_name_suffix = '_update_form'
    success_msg = "Daily Report updated!"

    def get(self, request, **kwargs):
        self.object = DailyReport.objects.get(id=self.kwargs['id'])
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def get_object(self, queryset=None):
        obj = DailyReport.objects.get(id=self.kwargs['id'])
        return obj

    def get_success_url(self):
        return reverse('dailyreport-list')


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
    template_name = 'careapp/diapering_create_form.html'
    success_msg = "Diapering completed"

    # def get_success_url(self):
    #     return reverse('childs-list')

    def diapering_create(request):
        '''
        Opens the initial diapering page
        '''

        if request.method == 'POST':
            form = DiaperingForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('diapering-create')
        else:
            form = DiaperingCreateView()
        return render(request, 'daily_report.html',
                      {'form': form})

    def get_success_url(self):
        return reverse('dailyreport-list')


class DiaperingUpdateView(DiaperingMixin, UpdateView):
    model = Diapering
    template_name_suffix = '_update_form'
    success_msg = "Diapering Session Added"

    def get(self, request, **kwargs):
        self.object = Diapering.objects.get(id=self.kwargs['id'])
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def get_object(self, queryset=None):
        obj = Diapering.objects.get(id=self.kwargs['id'])
        return obj

    def get_success_url(self):
        return reverse('dailyreport-list')


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

    def get(self, request, **kwargs):
        self.object = Sleeping.objects.get(id=self.kwargs['id'])
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def get_object(self, queryset=None):
        obj = Sleeping.objects.get(id=self.kwargs['id'])
        return obj

    def get_success_url(self):
        return reverse('dailyreport-list')


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

    def get(self, request, **kwargs):
        self.object = Eating.objects.get(id=self.kwargs['id'])
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def get_object(self, queryset=None):
        obj = Eating.objects.get(id=self.kwargs['id'])
        return obj

    def get_success_url(self):
        return reverse('dailyreport-list')

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
