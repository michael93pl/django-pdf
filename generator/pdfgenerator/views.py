from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from .forms import FileForm
from django.conf import settings
from django.utils.encoding import smart_str
from wsgiref.util import FileWrapper
import os
import pdfkit

def index(request):
    return render(request, "index.html")

def generate(request):
    if request.method == 'POST':
        form = FileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            passed = 'File name: ' + data['file_name'] + '     First name:' + data['first_name'] + '    Last name: ' + data['last_name']\
                     + '    Phone number: ' + str(data['phone_no']) + '    Data: ' + str(data['date'])
            file_name = form.cleaned_data['file_name']
            pdfpath = settings.MEDIA_ROOT
            name = "{}.pdf".format(file_name)
            filepath = os.path.join(pdfpath, name)
            pdfkit.from_string(passed, filepath)
            return render(request, 'aftergeneration.html', {'form': form})
    else:
        form = FileForm()
    return render(request, 'pdfform.html', {'form': form})

def download_file(request, file_name):

    file_path = settings.MEDIA_ROOT + file_name
    wrapper = FileWrapper(open(file_path, 'rb'))
    response = HttpResponse(wrapper, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=' + file_name
    return response

def list(request):
    folder = settings.MEDIA_ROOT
    file_list = os.listdir(folder)
    return render_to_response('list.html', {'file_list': file_list})


