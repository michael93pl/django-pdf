from django.shortcuts import render, redirect
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .forms import FileForm

def index(request):
    return render(request, "index.html")

def get_name(request):
    if request.method == 'POST':
        form = FileForm(request.POST)
        if form.is_valid():
            file_name = form.cleaned_data['file_name']
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename = "{}.pdf"'.format(file_name)
            p = canvas.Canvas(response)

            #sets local variable to avoid repetition
            data = form.cleaned_data
            passed = 'File name: ' + data['file_name'] + '     First name:' + data['first_name'] + '    Last name: ' + data['last_name']\
                     + '    Phone number: ' + str(data['phone_no']) + '    Data: ' + str(data['date'])
            p.drawString(0, 800, passed)
            p.showPage()
            p.save()
            return response
    else:
        form = FileForm()
    return render(request, 'pdfform.html', {'form': form})


def download_file(request):
    return render(request, 'download.html')
