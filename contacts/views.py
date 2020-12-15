from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
# Create your views here.


def contact(request):
    if request.method == 'POST' and request.user.is_authenticated:
        user = request.user
        query = request.POST['query']
        firstname = user.first_name
        lastname = user.last_name
        email = user.email
        contact = Contact(firstname=firstname,
                          lastname=lastname, email=email, query=query)
        contact.save()
        messages.info(request, "Query Submitted!")
        return redirect('contacts:contact')

    elif request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        query = request.POST['query']
        contact = Contact(firstname=firstname,
                          lastname=lastname, email=email, query=query)
        contact.save()
        messages.info(request, "Query Submitted!")

        return redirect('contacts:contact')

    context = {}
    return render(request, "contact/contact.html", context)
