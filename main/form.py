from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'topic', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name', 'class': 'contactInput'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'contactInput'}),
            'topic': forms.Select(attrs={'class': 'contactInput'}),
            'message': forms.Textarea(attrs={'placeholder': 'Enter your message', 'class': 'contactInput', 'rows': 5}),
        }