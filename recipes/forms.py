from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'steps', 'preparation_time', 'image', 'category']


class RecipeSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)


