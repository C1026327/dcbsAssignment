from django import forms
from django.core.mail import send_mail
from .models import Registration

class ContactForm(forms.Form):
    name = forms.CharField(max_length = 50)
    email = forms.EmailField()
    subject = forms.CharField(max_length = 100)
    message = forms.CharField(widget = forms.Textarea)

def send_mail(self):
    send_mail(self.cleaned_data.get('subject') + 
              ', sent on behalf of '+ 
              self.cleaned_data.get('name'), #Name
              self.cleaned_data.get('message'), #Contents
              self.cleaned_data.get('email'), #From
              ['longisland7629@gmail.com']) # Support Recipient, will not be changed in a regular circumstance, and cannot be modified outside of the code.
    ## Personal Email, functions with gmail, 
    ## might not work for other emails.

    ## You will need to change the email in ['longisland7629@gmail.com'], as this would be considered the "support email", which would be fixed.
    
class ModuleRegForm(forms.ModelForm):
    class Meta:
        model = Registration
        exclude = ['student', 'module', 'date_of_registration']