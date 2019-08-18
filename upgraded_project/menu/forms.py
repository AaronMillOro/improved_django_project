from django import forms
from django.core.exceptions import ValidationError
from django.forms.extras.widgets import SelectDateWidget

from .models import *

class MenuForm(forms.ModelForm):
    """ Extended form to change menu options """
    expiration_date = forms.DateField(
        widget=forms.extras.widgets.SelectDateWidget
    )

    class Meta:
        model = Menu
        exclude = ('created_date',)
        fields = (
            'season',
            'items',
            'expiration_date',
            )

    def clean_season(self):
        season = self.cleaned_data.get('season')
        if len(season) < 5:
            raise ValidationError('SEASON must have at least 5 characters')
        return season

    def clean_items(self):
        items = self.cleaned_data.get('items')
        if len(items) < 2:
            raise ValidationError('Select at least 2 ITEMS')
        return items
