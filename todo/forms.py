from django import forms

class TaskForm(forms.Form):
    task = forms.CharField(
    	label='Task',
    	widget=forms.TextInput(attrs={ 'class': 'form-control' }),
    	required=True,
    	strip=True,
    	max_length=160
    )
    progress = forms.IntegerField(
    	label='Progress',
    	widget=forms.NumberInput(attrs={ 'type': 'range', 'class': 'custom-range mt-3', 'step': '1' }),
    	required=True,
    	min_value=0,
    	max_value=100
    )
    deadline_date = forms.DateField(
    	label='Deadline',
    	widget=forms.DateInput(attrs={ 'type': 'date', 'class': 'form-control' }),
    	required=False
    )