# Generated by Django 3.1.4 on 2020-12-14 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20201214_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagecontrol',
            name='refernce_name',
            field=models.CharField(blank=True, help_text='Use a unique for the sections in the webpage', max_length=100, null=True, unique=True, verbose_name='Reference Name'),
        ),
    ]