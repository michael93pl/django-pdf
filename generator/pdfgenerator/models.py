from django.db import models

class Items(models.Model):
    file_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    birth = models.CharField(max_length=100)
    pesel = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    date = models.DateField()
