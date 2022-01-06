from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'full_name': form.cleaned_data['full_name'],
                'email': form.cleaned_data['email'],
                'contact_number': form.cleaned_data['contact_number'],
                'message': form.cleaned_data['message'],
                }
            message = "\n".join(body.values())

        try:
            send_mail(
                subject, message, 'admin@example.com', ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
            return redirect("home")
    form = ContactForm()
    return render(request, "contact/contact.html", {'form': form})
