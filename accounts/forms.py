from string import split
from django import forms
from django.forms import fields

class NorthwesternSignupForm(forms.Form):

	def save(self, user):
		user.save()

	def clean(self):
		if 'email' in self.cleaned_data:
			domain = split(self.cleaned_data['email'], '@')[1]
			if not 'northwestern.edu' in domain:
				raise forms.ValidationError('Northwestern University Emails Only')