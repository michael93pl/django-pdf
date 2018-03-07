from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.shortcuts import render_to_response, render
from django.utils.crypto import get_random_string
from django.http import HttpResponse
from django.conf import settings
from django.views import View
from wsgiref.util import FileWrapper
import os
import pdfkit
import datetime
from .forms import FileForm, KeyForm
from .models import Items

def index(request):
    return render(request, "index.html")

@shared_task()
def creation(data):
    passed = data['file_name'] + data['first_name'] + data['last_name'] + data['birth'] + data['pesel']\
    + str(data['email']) +str(data['phone_no']) + data['street'] + data['city'] + data['code']
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
            time = datetime.datetime.now()  # displays current time
            key = get_random_string(length=10)  # generates secret 10 char long key
            name = form.cleaned_data['file_name'] + '.pdf'
            file = Items()
            file.file_name = name
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
            file.file = settings.MEDIA_ROOT
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

# Iv5R7W6H0M
def list(request):
    folder = settings.MEDIA_ROOT
    file_list = os.listdir(folder)
    form = KeyForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            name = request.POST['name']  # filename given by the user
            secret = form.cleaned_data['secret_key']  # key given by the user
            taken = (name, secret)  # converts data to tuple
            given = Items.objects.filter(file_name=name).values_list('file_name', 'secret').first()  # returns tuple
            if taken == given:
                file_name = name
                file_path = settings.MEDIA_ROOT + file_name
                wrapper = FileWrapper(open(file_path, 'rb'))
                response = HttpResponse(wrapper, content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename=' + file_name
                return response
    return render(request, 'list.html', {'form': form, 'file_list': file_list})
