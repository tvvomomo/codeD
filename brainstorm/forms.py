from django import forms

class AddWordForm(forms.Form):
	word = forms.CharField(max_length = 30)
#	link = forms.URLField(blank = True)