from django import forms
from tasks.models import TasksEntry
from django.contrib.auth.models import User

options = [
    ('Win','win'),
    ('Loss', 'loss'),
]

class TasksEntryForm(forms.ModelForm):
	opposing = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))
	win = forms.CharField(widget=forms.Select(choices=options))
	class Meta():
		model = TasksEntry
		fields = ('opposing', 'win')
