# Generated by Django 3.1.4 on 2020-12-14 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20201214_1932'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pagecontrol',
            old_name='refernce_name',
            new_name='reference_name',
        ),
    ]
