from django import forms
from django.core.exceptions import ValidationError
from django.forms.extras.widgets import SelectDateWidget
from datetime import datetime

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

    #def clean_season(self):
    #    season = self.clean_data.get('season')
    #    if len(season) < 5:
    #        raise ValidationError('SEASON name must have at least 5 characters')
        #elif len(items) < 1:
        #    raise ValidationError('Select at least 1 ITEM')
    #    return season
