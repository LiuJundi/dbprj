from django import forms
from .models import Customer

# class CustomerForm(forms.ModelForm):
# 	class Meta:
# 		model = Customer
# 		fields = ['cellphone', 'firstName', 'lastName']

class SignUpForm(forms.Form):
	cellphone = forms.CharField(required=True)
	firstName = forms.CharField(required=True)
	lastName = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput() )
	password2 = forms.CharField(required=True, widget=forms.PasswordInput() )

	def clean_cellphone(self):
		cellphone = self.cleaned_data.get('cellphone')
		if len(cellphone) != 11:
			raise forms.ValidationError("Invalid cellphone number. Please input 11 digits.")
		return cellphone





