from django.db import models

# Create your models here.

# Home Page models:


class Page(models.Model):

    # This model will store the pages of the website and the permalinks
    # This enables the admin to select a link for a button he wants to customize

    page_title = models.CharField(
        'Page Title', max_length=100)
    page_permalink = models.CharField(
        'Page PermaLink', max_length=100)

    def __str__(self):
        return self.page_title


class FeatureInfo(models.Model):
    # Features of the PDF editor apps shown in home page and here's the database:

    features_name = models.CharField(
        'Feature Title', max_length=100)
    feature_icon_html = models.CharField(
        'Feature icon HTML tag', max_length=100)

    def __str__(self):
        return self.features_name


class Stat(models.Model):
    # Stats of the PDF editor apps shown in home page and here's the database:

    stat_header_text = models.CharField('Stats Header Text', max_length=50)
    stat_des_text = models.TextField('Stats Description Text', max_length=255)

    def __str__(self):
        return self.stat_header_text


class Card(models.Model):

    card_title = models.CharField(
        'Reference Name', max_length=100, blank=True, null=True)
    card_icon_html = models.CharField(
        'Header icon HTML tag', max_length=100)
    card_des_text = models.TextField('Caed Description Text', max_length=255)
    card_button_text = models.CharField('Card Button Text', max_length=255)
    button_target_page = models.ForeignKey(
        Page, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.card_title


class SectionLayoutType(models.Model):
    section_title = models.CharField('Section Title', max_length=100)
    has_heading = models.BooleanField('Section has Heading?', default=False)
    has_banner_img = models.BooleanField(
        'Section has banner Image?', default=False)
    has_description = models.BooleanField(
        'Section has description?', default=False)
    has_button = models.BooleanField('Section has button?', default=False)
    has_stats = models.BooleanField('Section has stats?', default=False)
    has_card = models.BooleanField('Section has card?', default=False)
    has_feature_list = models.BooleanField(
        'Section has Features List?', default=False)

    def __str__(self):
        return self.section_title


class PageControl(models.Model):
    reference_name = models.CharField(
        'Reference Name', max_length=100, null=True, blank=True, help_text="Use a unique for the sections in the webpage", unique=True)
    source_page = models.ForeignKey(
        Page, related_name='Source', on_delete=models.SET_NULL, null=True, blank=True)
    section_type = models.ForeignKey(
        SectionLayoutType, on_delete=models.SET_NULL, null=True, blank=True)
    heading_text = models.CharField(
        'Heading Text', max_length=100, null=True, blank=True)
    description_text = models.TextField(
        'Description Text', max_length=1000, null=True, blank=True)
    button_text = models.CharField(
        'Button Text', max_length=100, null=True, blank=True)
    button_target_page = models.ForeignKey(
        Page, related_name='Button', on_delete=models.SET_NULL, null=True, blank=True)
    banner_image = models.ImageField(
        upload_to='sections', blank=True, null=True)
    card_list = models.ManyToManyField(
        Card, max_length=100, blank=True)
    Stat_list = models.ManyToManyField(
        Stat, max_length=100, blank=True)
    feature_list = models.ManyToManyField(
        FeatureInfo, max_length=100, blank=True)

    def __str__(self):
        return self.reference_name
