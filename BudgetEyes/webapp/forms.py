
from django.contrib.auth import authenticate

from django import forms

class CurrencyForm(forms.Form):
  currency_name = forms.CharField(max_length=10)
  new_value = forms.IntegerField(max_value=100, min_value=0)


class LoginForm(forms.Form):
  required_css_class = 'required'
  username = forms.CharField(max_length=30)
  password = forms.CharField(max_length=32, widget=forms.PasswordInput)
"""
  def clean(self):
    super(LoginForm, self).clean()

    username = self.cleaned_data.get("username")
    password = self.cleaned_data.get("password")

    user = authenticate(username=username, password=password)
    
    if not user:
      raise forms.ValidationError("No user with those credentials")
"""    


class RegisterForm(forms.Form):
  firstname = forms.CharField(max_length=40, label="First name")
  lastname = forms.CharField(max_length=40, label="Last name")
  username = forms.CharField(max_length=40, label="Username")
  email = forms.EmailField(max_length=20, label="Email")
  password = forms.CharField(max_length=128, label="Pasword", widget=forms.PasswordInput) 
  re_password = forms.CharField(max_length=128, label="Enter password again", widget=forms.PasswordInput)

  def clean(self):
    super(RegisterForm, self).clean()
    password = self.cleaned_data.get("password")
    re_pass = self.cleaned_data.get("re_password")

    if not password == re_pass:
      self.add_error('re_password', "Passwords must match")