from django.db import models

class Items(models.Model):
    file_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth = models.CharField(max_length=100)
    pesel = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.IntegerField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    date = models.DateField()
