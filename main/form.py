from django import forms
from .models import Contact, MovieReview

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


class MovieReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = ['starRating', 'review']
        labels = {
            'starRating': 'Your rating',
            'review': 'Your review',
        }
        widgets = {
            'starRating': forms.Select(
                choices=[(rating, f'{rating} / 5') for rating in range(1, 6)],
                attrs={'class': 'review-input'},
            ),
            'review': forms.Textarea(
                attrs={
                    'class': 'review-input',
                    'placeholder': 'What did you think about this movie?',
                    'rows': 5,
                }
            ),
        }