from django import forms

class FileForm(forms.Form):
    file_name = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone_no = forms.IntegerField()
    date = forms.DateField()






