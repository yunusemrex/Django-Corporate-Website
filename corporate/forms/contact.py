from django import forms
from corporate.models import ContactModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ('full_name','subject','email', 'message',)