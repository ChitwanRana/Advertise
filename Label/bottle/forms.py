from django import forms
from .models import FSSAIEntry, Review


class FSSAIEntryForm(forms.ModelForm):
    date_of_delivery = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        })
    )

    class Meta:
        model = FSSAIEntry
        fields = ['fssai_code', 'authorisation_name', 'date_of_delivery', 'number_of_orders', 'logo', 'certificate']
        widgets = {
            'authorisation_name': forms.TextInput(attrs={
                'placeholder': 'e.g., Fresh Foods Pvt Ltd',
                'class': 'form-control'
            }),
            'fssai_code': forms.TextInput(attrs={
                'placeholder': 'e.g., 12345678901234',
                'class': 'form-control'
            }),
            'number_of_orders': forms.NumberInput(attrs={
                'min': 0,
                'placeholder': '100',
                'class': 'form-control'
            }),
            'logo': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'certificate': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,image/*'
            }),
        }
        labels = {
            'fssai_code': 'FSSAI License Number',
            'authorisation_name': 'Business / Brand Name',
            'date_of_delivery': 'Expected Delivery Date',
            'number_of_orders': 'Number of Bottles',
            'logo': 'Brand Logo',
            'certificate': 'FSSAI Certificate',
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'rating', 'feedback']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your name',
                'class': 'form-control'
            }),
            'rating': forms.Select(attrs={
                'class': 'form-select'
            }),
            'feedback': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Share your thoughts about this label design...',
                'class': 'form-control'
            }),
        }
        labels = {
            'name': 'Your Name',
            'rating': 'Rating (1-5 stars)',
            'feedback': 'Your Review',
        }
from django import forms
from .models import FSSAIEntry, Review

class FSSAIEntryForm(forms.ModelForm):
    class Meta:
        model = FSSAIEntry
        fields = ['fssai_code', 'authorisation_name', 'date_of_delivery', 'number_of_orders', 'logo', 'certificate']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'rating', 'feedback']
