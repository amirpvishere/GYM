from django.shortcuts import render
from .models import Contact


def item(request):
    items = Contact.objects.all()
    return render(request, 'ContactUs/items.html', {'items': items})


def contact(request):
    if request.method == 'POST':
        name = request.GET.get('fname')
        email = request.GET.get('email')
        phone = request.GET.get('phone')
        message = request.GET.get('message')
        Contact.objects.create(name=name, email=email, phone=phone, message=message)
    return render(request, "ContactUs/contact.html")


