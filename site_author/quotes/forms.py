from django.forms import ModelForm, CharField, TextInput
from .models import AuthorAdd, QuoteAdd


class AuthorForm(ModelForm):
    name = CharField(min_length=3, max_length=30, required=True, widget=TextInput(attrs={'class': "form-control"}))

    class Meta:
        model = AuthorAdd
        fields = ['name']


class QuoteForm(ModelForm):
    quote = CharField(min_length=5, max_length=250, required=True, widget=TextInput(attrs={'class': "form-control"}))
    author = CharField(min_length=3, max_length=30, required=True, widget=TextInput(attrs={'class': "form-control"}))

    class Meta:
        model = QuoteAdd
        fields = ['quote', 'author']


