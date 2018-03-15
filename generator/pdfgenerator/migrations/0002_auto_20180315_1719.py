# Generated by Django 2.0.2 on 2018-03-15 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfgenerator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='items',
            name='city',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='items',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='items',
            name='file_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='items',
            name='phone_no',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='items',
            name='street',
            field=models.CharField(max_length=100),
        ),
    ]
