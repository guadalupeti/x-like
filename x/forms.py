from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 100, label = 'Username', required = True)
    password = forms.CharField(max_length = 100, label = 'Password', required = True, widget = forms.PasswordInput)

class PostForm(forms.Form):
    text = forms.CharField(max_length = 240, widget = forms.Textarea(attrs = {'rows': 4, 'cols': 40}), required = True)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 100, label = 'Username', required = True)
    email = forms.CharField(max_length = 100, label = 'Email', required = True)
    password = forms.CharField(max_length = 100, label = 'Password', required = True, widget = forms.PasswordInput)
    confirm_password = forms.CharField(max_length = 100, label = 'Confirm Password', required = True, widget = forms.PasswordInput)