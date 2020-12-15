# Generated by Django 3.1.4 on 2020-12-13 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(max_length=100, verbose_name='Page Title')),
                ('page_permalink', models.CharField(max_length=100, verbose_name='Page Perma Link')),
            ],
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stats_header_text', models.CharField(max_length=50, verbose_name='Stats Header Text')),
                ('stats_title_text', models.CharField(max_length=50, verbose_name='Stats Title Text')),
                ('stats_des_text', models.CharField(max_length=255, verbose_name='Stats Description Text')),
            ],
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('features_header_text', models.CharField(max_length=255, verbose_name='Features Header Text')),
                ('feature_title', models.CharField(max_length=255, verbose_name='Feature title')),
                ('feature_icon_tag', models.CharField(max_length=100, verbose_name='Feature icon HTML tag')),
                ('features_button_text', models.CharField(max_length=255, verbose_name='Features Button Text')),
                ('button_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.pages')),
            ],
        ),
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_header_icon_tag', models.CharField(max_length=100, verbose_name='Header icon HTML tag')),
                ('card_des_text', models.CharField(max_length=255, verbose_name='Caed Description Text')),
                ('card_button_text', models.CharField(max_length=255, verbose_name='Card Button Text')),
                ('button_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.pages')),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_header_text', models.CharField(max_length=255, verbose_name='Banner Header Text')),
                ('banner_button_text', models.CharField(max_length=255, verbose_name='Banner Button Text')),
                ('button_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.pages')),
            ],
        ),
    ]