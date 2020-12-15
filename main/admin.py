from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    pass


admin.site.register(FeatureInfo)
admin.site.register(Stat)
admin.site.register(SectionLayoutType)
admin.site.register(PageControl)
admin.site.register(Card)
