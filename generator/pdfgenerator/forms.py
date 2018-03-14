from django import forms
from django.core.validators import RegexValidator, EmailValidator
from django.core.exceptions import ValidationError

# cheks if names don't contain numbers
character_validator = RegexValidator(regex='^[a-zA-Z]*$',
                                     message='Please provide your first and last name with characters only.',
                                     code='invalid_username')

# Validates file name
file_validator = RegexValidator(regex='^[a-zA-Z0-9./-_]*$',
                                message='Please provide valid name.',
                                code='invalid_name')

# Validates names
name_validator = RegexValidator(regex='^[a-zA-Z0-9./-_\s]*$',
                                message='Please provide valid name.',
                                code='invalid_name')


# Validates phone number
number_validator = RegexValidator(regex='^[0-9-/\s]*$',
                                  message='Please provide valid phone number.',
                                  code='invalid_number')


# Zip code validator
code_validator = RegexValidator(regex='^[0-9-\s]*$',
                                message='Please provide valid zip code.',
                                code='invalid_number')


# Validates PESEL number based on Form requirements
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

#Form used to generate pdf
class FileForm(forms.Form):
    file_name = forms.CharField(max_length=20, required=True, validators=[file_validator])
    first_name = forms.CharField(max_length=20, required=True, validators=[character_validator])
    last_name = forms.CharField(max_length=30, required=True, validators=[character_validator])
    birth = forms.DateField(required=True, input_formats=['%d-%m-%Y',
                                                          '%d/%m/%Y',
                                                          '%d.%m.%Y',
                                                          '%Y-%m-%d',
                                                          '%Y/%m/%d',
                                                          '%Y.%m.%d'
                                                          ])
    pesel = forms.CharField(max_length=11, required=True, validators=[check_pesel])
    email = forms.EmailField(max_length=30, required=True, validators=[EmailValidator])
    phone_no = forms.CharField(min_length=9, max_length=11, required=True, validators=[number_validator])
    street = forms.CharField(max_length=30, required=True, validators=[name_validator])
    city = forms.CharField(max_length=30, required=True, validators=[character_validator])
    code = forms.CharField(min_length=5, max_length=6, required=True, validators=[code_validator])


#Form used to validate permission
class KeyForm(forms.Form):
    secret_key = forms.CharField(max_length=100, required=True)
