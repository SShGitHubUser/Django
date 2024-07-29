from django import forms

from .models import CustomerReview


class CustomerReviewForm(forms.ModelForm):
    class Meta:
        model = CustomerReview
        fields = '__all__'
