from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FileForm
import os
import pdfkit

def index(request):
    return render(request, "index.html")

def get_name(request):
    if request.method == 'POST':
        form = FileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            passed = 'File name: ' + data['file_name'] + '     First name:' + data['first_name'] + '    Last name: ' + data['last_name']\
                     + '    Phone number: ' + str(data['phone_no']) + '    Data: ' + str(data['date'])
            file_name = form.cleaned_data['file_name']
            pdfpath = '/home/galander/Desktop/Projekty/django-pdf-generator/django-pdf/generator/static/pdfs'
            name = "{}.pdf".format(file_name)
            filepath = os.path.join(pdfpath, name)
            pdfkit.from_string(passed, filepath)

            return HttpResponse("ALL GOOD SIR !")
    else:
        form = FileForm()
    return render(request, 'pdfform.html', {'form': form})

#def download_file(request):
    #pdf = pdfkit.from_url('http://127.0.0.1:8000/pdf', False)
    #response = HttpResponse(pdf, content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="nowy.pdf"'

    #return response


