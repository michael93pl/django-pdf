from django import forms
from django.core.validators import RegexValidator, EmailValidator
from django.core.exceptions import ValidationError

# cheks if names don't contain numbers
character_validator = RegexValidator(regex='^[a-zA-Z]*$', message='Please provide your first and last name with characters only.',
                                     code='invalid_username')

# validates pesel numer - doesn't check gender number since we don't ask for a gender
def check_pesel(value):
    sum, multi = 0, [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
    exceptions = (22222222222, 44444444444, 66666666666, 88888888888)
    x = [int(x) for x in str(value)]  # returns pesel as list of ints
    for i in range(11):
        sum += (int(x[i] * multi[i]))
    x = str(sum)[-1] == '0'  # returns True or False
    if value in exceptions:
        raise ValidationError('PESEL is incorrect')
    if x != True:
        raise ValidationError('PESEL is incorrect')


number_validator = RegexValidator(regex='^[0-9]*$', message='Please provide valid phone number',
                                  code='invalid_number')


class FileForm(forms.Form):
    file_name = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100, required=True, validators=[character_validator])
    last_name = forms.CharField(max_length=100, required=True, validators=[character_validator])
    address = forms.CharField(max_length=100)
    email = forms.EmailField(required=True, validators=[EmailValidator])
    #birth = forms.CharField(max_length=100)
    pesel = forms.CharField(max_length=11, required=True, validators=[check_pesel])
    phone_no = forms.CharField(max_length=9, required=True, validators=[number_validator])


