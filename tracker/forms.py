from django import forms
from .models import FoodSpot


class FoodSpotForm(forms.ModelForm):
    available_until = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        required=False
    )
    latitude = forms.FloatField(widget=forms.HiddenInput())
    longitude = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = FoodSpot
        fields = ['food_type', 'description', 'latitude',
                  'longitude', 'available_until', 'photo']
