from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.conf import settings


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Enquiry'
            body = {
                'full_name': form.cleaned_data['full_name'],
                'email': form.cleaned_data['email'],
                'contact_number': form.cleaned_data['contact_number'],
                'message': form.cleaned_data['message'],
                }
            message = '\n'.join(body.values())
            form.save()

        try:
            send_mail(
                subject, message, 'admin@example.com', ['admin@example.com', 'sb4_cbu@yahoo.com', 'cia.ribka@gmail.com'])
            return render(request, 'contact/contact_success.html')
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
           
    form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
