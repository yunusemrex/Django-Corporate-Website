from django.shortcuts import render, redirect
from corporate.models import ContactModel
from corporate.forms import ContactForm
from corporate.views.sent_email import sent_email

def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('sent-email')
    
    return render(request, 'pages/contact-page.html', context = {
         'form':form
     })

