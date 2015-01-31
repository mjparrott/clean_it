from django import forms

class SignUpForm(forms.Form):
  user_name = forms.CharField(label='Your name', max_length=100)
  email = forms.CharField(label='Your email', max_length=100)
  password = forms.CharField(label='Your password', max_length=100)
