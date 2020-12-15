from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):

    # Grabbing all the objects in PageControl model which is for Home Page!
    sections = PageControl.objects.filter(source_page__page_title='Home Page')

    context = {
        'sections': sections,
    }
    return render(request, "homepage/index.html", context)


@login_required(login_url='/accounts/login/?pagerequireslogin')
def download(request):

    sections = PageControl.objects.filter(
        source_page__page_title='Download Page')

    context = {

        'sections': sections,

    }
    return render(request, "download/download.html", context)


def about(request):

    sections = PageControl.objects.filter(source_page__page_title='About Us')

    context = {
        'sections': sections,
    }
    return render(request, "about/about.html", context)
