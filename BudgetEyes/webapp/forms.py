from django import forms

class CurrencyForm(forms.Form):
  currency_name = forms.CharField(max_length=10)
  new_value = forms.IntegerField(max_value=100, min_value=0)