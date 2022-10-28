from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import *

from .forms import CSVFileForm
from .models import Journey
from utils import polestar_log_parser


class HomePage(TemplateView):
    template_name = 'home.html'
    

class ShowAllJourneys(ListView):
    template_name = 'journeys.html'
    model = Journey
    context_object_name = 'journeys'


def parse_log_file(file):
    print('lets play with the file')
    return


def upload_log_file(request):
    if request.method == 'POST':
        form = CSVFileForm(request.POST, request.FILES)
        if form.is_valid():
            polestar_log_parser.parse(request.FILES['polestar_log_file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = CSVFileForm()
    return render(request, 'upload.html', {'form': form})