from django import forms

from report.models import Entry


class EntryAddForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('date', 'distance', 'duration')
