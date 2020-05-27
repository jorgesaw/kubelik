"""Contacts form."""

# Django
from django import forms


class ContactForm(forms.Form):
	"""Contact form."""

	first_name = forms.CharField(
		label='Nombre', 
		max_length=255, 
		required=True, 
		widget=forms.TextInput(
			attrs={'class': 'form-control', 'autofocus': 'autofocus'}, 
		), min_length=3
	)
	last_name = forms.CharField(
		label='Apellido', 
		max_length=255, 
		required=True, 
		widget=forms.TextInput(
			attrs={'class': 'form-control'}, 
		), min_length=3
	)
	email = forms.EmailField(
		label='Email', 
		required=True, 
		widget=forms.EmailInput(
			attrs={'class': 'form-control'}, 
		)
	) 
	message = forms.CharField(
		label='Mensaje', 
		required=True, 
		widget=forms.Textarea(
			attrs={'class': 'form-control', 'cols': 30, 'rows': 10}, 
		), min_length=10
	)

	