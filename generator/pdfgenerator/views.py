from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import NameForm

def index(request):
    return render(request, "index.html")

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return render(request, 'aftergeneration.html', {'form': form})
    else:
        form = NameForm()
    return render(request, 'pdfform.html', {'form': form})

def after_submit(request):
    pass

def download_file(request):
    return render(request, 'download.html')
