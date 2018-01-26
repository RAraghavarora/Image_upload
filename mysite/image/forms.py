from django import forms

class ProfileForm(forms.Form):
   name = forms.CharField(max_length = 100)
   picture = forms.ImageField(label = 'Select a file')

class NewForm(forms.Form):
	name = forms.CharField(max_length = 100)
	picture = forms.ImageField(label= 'Please fill all the fields')