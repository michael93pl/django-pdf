from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm

def index(request):
    return render(request, "index.html")

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()

    return render(request, 'pdfform.html', {'form': form})

