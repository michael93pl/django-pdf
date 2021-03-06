from django.db import models
from django.utils.html import format_html


class Items(models.Model):
    file_name = models.CharField(max_length=40)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    birth = models.DateField()
    pesel = models.CharField(max_length=11)
    email = models.EmailField(max_length=50)
    phone_no = models.CharField(max_length=17)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=35)
    code = models.CharField(max_length=6)
    date = models.DateField()
    secret = models.CharField(max_length=10)

    def __str__(self):
        return self.file_name

    def view_link(self):
        return format_html("<a href='/download/{}'>{}</a>".format(self.file_name, self.file_name))
    view_link.short_description = ''
    view_link.allow_tags = True



