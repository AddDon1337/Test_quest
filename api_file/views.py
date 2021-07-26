from django.shortcuts import render
from .forms import CsvForm


# Create your views here.
def home_view(request):
    context = {}

    context['form'] = CsvForm()

    return render(request, "home.html", context)
