from django.db import models
from generator.settings import MEDIA_ROOT


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
    secret = models.CharField(max_length=10)
    file = models.FilePathField(path=MEDIA_ROOT)

    def __str__(self):
        return self.file_name

    def file_link(self):
        if self.file:
            return "<a href='%s'>download</a>" % (self.file)
        else:
            return "No attachment"

    file_link.allow_tags = True

