from django import forms
from .models import Event, Detail


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_host', 'event_cover']

class DetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = ['description', 'place', 'time']




