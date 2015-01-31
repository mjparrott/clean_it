from django import forms

class SignUpForm(forms.Form):
  user_name = forms.CharField(label='Your name', max_length=100)
  email = forms.EmailField(label='Your email', max_length=100)
  password = forms.CharField(label='Your password', max_length=100, widget = forms.PasswordInput())

class LoginForm(forms.Form):
  user_name = forms.CharField(label='Your name', max_length=100)
  password = forms.CharField(label='Your password', max_length=100, widget = forms.PasswordInput())

class CreateGroupForm(forms.Form):
  group_name = forms.CharField(label='Group name', max_length=100)

class AddToGroupForm(forms.Form):
  member_name = forms.CharField(label='Member name', max_length=100)

class AddTaskForm(forms.Form):
  task_name = forms.CharField(label='Task', max_length=100)
  weight = forms.IntegerField(label = 'Weighting', max_value = 5, min_value = 1)
  freq = forms.IntegerField(label = 'Frequency', max_value = 3, min_value = 1, help_text = '1 = daily, 2 = weekly, 3 = monthly')
