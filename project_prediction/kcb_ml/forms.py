from django import forms

class SearchForm(forms.Form):
    amt = forms.CharField(label = "ID",max_length =200)
