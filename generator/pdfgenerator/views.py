from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.shortcuts import render
from django.utils.crypto import get_random_string
from django.http import HttpResponse
from django.conf import settings
from django.views import View
from wsgiref.util import FileWrapper
import pandas as pd
import os
import pdfkit
import datetime
from .forms import FileForm, KeyForm
from .models import Items


# homepage
class Index(View):

    def get(self, request):
        return render(request, "index.html")

@shared_task()
def creation(data):
    passed = data['file_name'] + data['first_name'] + data['last_name'] + data['birth'] + data['pesel']\
    + str(data['email']) +str(data['phone_no']) + data['street'] + data['city'] + data['code']
    file_name = data['file_name']
    pdf_path = settings.MEDIA_ROOT
    name = "{}.pdf".format(file_name)
    file_path = os.path.join(pdf_path, name)
    pdfkit.from_string(passed, file_path)
    return True


# filling a form view
class Generate(View):
    form_class = FileForm
    generate_template = 'pdfform.html'

    def post(self, request):
        form = self.form_class(request.POST)
        if request.FILES:
            csvfile = request.FILES['csv_file']
            file_data = pd.read_csv(csvfile)
            rows = []
            for line in file_data:
                rows.append(line)
            first = rows[0]
            last = rows[1]
            birth = rows[2]
            pesel = rows[3]
            email = rows[4]
            phone = rows[5]
            street = rows[6]
            city = rows[7]
            code = rows[8]

            data = {'first_name': first,
                    'last_name': last,
                    'birth': birth,
                    'pesel': pesel,
                    'email': email,
                    'phone_no': phone,
                    'street': street,
                    'city': city,
                    'code': code}

            form = self.form_class(initial=data)

        if form.is_valid():
            # gather all data to the model
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
            file.file = '/download/' + name
            file.save()

            context = {
                'form': form,
                'time': time,
                'key': key
                      }

            data = form.cleaned_data
            creation.delay(data)  # passes data to celery task
            return render(request, 'aftergeneration.html', context)
        else:
            return render(request, self.generate_template, {'form': form})

    def get(self, request):
        form = self.form_class
        return render(request, self.generate_template, {'form': form})


# downloads file
def download_file(request, file_name):
    file_path = settings.MEDIA_ROOT + file_name
    wrapper = FileWrapper(open(file_path, 'rb'))
    response = HttpResponse(wrapper, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=' + file_name
    return response


# listing and checking whether keys match
class List(View):
    form_class = KeyForm
    folder = settings.MEDIA_ROOT

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            name = request.POST['name']  # filename given by the user
            secret = form.cleaned_data['secret_key']  # key given by the user
            taken = (name, secret)  # converts data to tuple
            given = Items.objects.filter(file_name=name).values_list('file_name', 'secret').first()  # returns tuple
            if taken == given:# checks whether keys match
                file_name = name
                file_path = self.folder + file_name
                wrapper = FileWrapper(open(file_path, 'rb'))
                response = HttpResponse(wrapper, content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename=' + file_name
                return response
            else:
                return HttpResponse("Please go back and provide valid secret key!")

    def get(self, request):
        file_list = os.listdir(self.folder)
        form = self.form_class
        return render(request, 'list.html', {'form': form, 'file_list': file_list})
