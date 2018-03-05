from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.shortcuts import render_to_response, render
from django.utils.crypto import get_random_string
from django.http import HttpResponse
from django.conf import settings
from wsgiref.util import FileWrapper
import os
import pdfkit
import datetime
from .forms import FileForm, KeyForm
from .models import Items

def index(request):
    return render(request, "index.html")

# DO POPRAWY !!!
@shared_task()
def creation(data):
    passed = 'File name: ' + data['file_name'] + '     First name:' + data['first_name'] + '    Last name: ' + data[
        'last_name'] \
             + '    Phone number: ' + str(data['phone_no'])
    file_name = data['file_name']
    pdfpath = settings.MEDIA_ROOT
    name = "{}.pdf".format(file_name)
    filepath = os.path.join(pdfpath, name)
    pdfkit.from_string(passed, filepath)
    return True

def generate(request):
    if request.method == 'POST':
        form = FileForm(request.POST)
        if form.is_valid():
            time = datetime.datetime.now()
            key = get_random_string(length=10)
            file = Items()
            file.file_name = form.cleaned_data['file_name']
            file.first_name = form.cleaned_data['first_name']
            file.last_name = form.cleaned_data['last_name']
            file.birth = form.cleaned_data['birth']
            file.pesel = form.cleaned_data['pesel']
            file.email = form.cleaned_data['email']
            file.phone_no = form.cleaned_data['phone_no']
            file.street = form.cleaned_data['street']
            file.city = form.cleaned_data['city']
            file.code = form.cleaned_data['code']
            file.date = time
            file.secret = key
            file.save()

            context = {
                'form': form,
                'time': time,
                'key': key
            }
            data = form.cleaned_data
            creation.delay(data)
            return render(request, 'aftergeneration.html', context)
        else:
            return render(request, 'pdfform.html', {'form': form})
    else:
        form = FileForm()
    return render(request, 'pdfform.html', {'form': form})

def download_file(request, file_name):
    file_path = settings.MEDIA_ROOT + file_name
    wrapper = FileWrapper(open(file_path, 'rb'))
    response = HttpResponse(wrapper, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=' + file_name
    return response

# Iv5R7W6H0M
def list(request):
    folder = settings.MEDIA_ROOT
    file_list = os.listdir(folder)
    form = KeyForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            #secret = form.cleaned_data['secret_key']
            #obj = Items.objects.get(secret=secret)
            return render(request, 'list.html', {'form': form, 'file_list': file_list})
    return render(request, 'list.html', {'form': form, 'file_list': file_list})
