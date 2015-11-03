from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, ListView
from django.shortcuts import render, redirect
from datetime import datetime
from .models import Child
from .forms import ChildForm
from django.contrib.auth.decorators import login_required
# Create your views here.


# returns current time in html
def index(request):
    now = datetime.now()
    html = "<html><body>Hello world. It is now {} local server time.</body></html>".format(
        now)
    return HttpResponse(html)


class ListChildView(ListView):

    model = Child
    template_name = 'careapp/children_list.html'


class CreateChildView(CreateView):

    model = Child
    template_name = 'careapp/edit_child.html'

    def get_success_url(self):
        return reverse('children-list')


# @login_required
def add_child(request):
    if request.method == 'POST':
        form = ChildForm(request.POST)
        if form.is_valid():
            child = form.save(commit=False)
            child.modified = datetime.now()
            child.save()
            return redirect('children-list')
    else:
        form = ChildForm()
    return render(request, 'edit_child.html',
                  {'form': form})
