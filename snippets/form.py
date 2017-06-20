from django import forms
from django.forms import ModelForm
from .models import Snippet

class SnippetForm(forms.Form):
    snippet_title = forms.CharField(label="Title", max_length = 80)
    snippet_language = forms.CharField(label="Language", max_length = 50)
    snippet_code = forms.CharField(label="Code Snippet", max_length = 2000)
    snippet_description = forms.CharField(label = "Description", max_length = 2000)
    snippet_author = forms.CharField(label= "Author", max_length = 100)
