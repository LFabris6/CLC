from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class NewUserForm(UserCreationForm):

	
	class Meta:
		model = User
		fields = ["password1", "password2", "email"]

	def __init__(self, *args, **kwargs):
		super(NewUserForm, self).__init__(*args, **kwargs)
		self.fields['email'].required = True

	def save(self, commit=True):
		email = self.cleaned_data["email"]

		user = super(NewUserForm, self).save(commit=False)
		user.email = email
		
		
		for i in range(len(email)):
			if(email[i] == "@"):
				name = "".join(email[0:i])
		
		user.username = name
				

		if commit:
			user.save()
		return user

	



class LoginForm(forms.Form):
	email = forms.CharField(max_length=50)
	password = forms.CharField(max_length=30, widget=forms.PasswordInput)