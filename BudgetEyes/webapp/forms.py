from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from django import forms

class CurrencyForm(forms.Form):
  currency_name = forms.CharField(max_length=10)
  new_value = forms.IntegerField(max_value=100, min_value=0)


class LoginForm(forms.Form):
  required_css_class = 'required'
  username = forms.CharField(max_length=30)
  password = forms.CharField(max_length=32, widget=forms.PasswordInput)

  def clean(self):
    super(LoginForm, self).clean()

    username = self.cleaned_data.get("username")
    password = self.cleaned_data.get("password")

    user = authenticate(username=username, password=password)
    
    if not user:
      raise forms.ValidationError("No user with those credentials")
    
