from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, ListView

from .models import Child
# Create your views here.


def index(request):
    return HttpResponse("hello. world.test 10:24pm")


# class ListChildView(ListView):
#
#     model = Child
#     template_name = 'children_list.html'
#
#
# class CreateChildView(CreateView):
#
#     model = Child
#     template_name = 'edit_child.html'
#
#     def get_success_url(self):
#         return reverse('children-list')
