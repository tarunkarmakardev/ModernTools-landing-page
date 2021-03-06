# Generated by Django 3.1.4 on 2020-12-14 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_pagecontrol_banner_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='card_des_text',
            field=models.TextField(max_length=255, verbose_name='Caed Description Text'),
        ),
        migrations.AlterField(
            model_name='pagecontrol',
            name='description_text',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Description Text'),
        ),
        migrations.AlterField(
            model_name='stat',
            name='stat_des_text',
            field=models.TextField(max_length=255, verbose_name='Stats Description Text'),
        ),
    ]
