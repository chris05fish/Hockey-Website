from django import forms
from budget.models import BudgetEntry
from django.contrib.auth.models import User

options = [
    ('Rightwing','rightwing'),
    ('Leftwing', 'leftwing'),
    ('Defensemen', 'defensemen'),
    ('Center', 'center'),
    ('Goaltender', 'goaltender'),
]

class BudgetEntryForm(forms.ModelForm):
    player = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))
    position = forms.CharField(widget=forms.Select(choices=options))
    points = forms.IntegerField(widget=forms.TextInput(attrs={'size': '80'}))
    prediction = forms.IntegerField(widget=forms.TextInput(attrs={'size': '80'}))
    class Meta():
        model = BudgetEntry
        fields = ('player', 'position', 'points', 'prediction')
