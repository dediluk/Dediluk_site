from django.forms import ModelForm
from .models import Book, Author
from django import forms


class CreateBookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'description',
            'image',
            'author_name'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'rows': 2,
                'placeholder': 'Название'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Описание',
                'rows': 5
            }),
            'author_name': forms.SelectMultiple(attrs={
                'multiple': 'multiple',
                'size': 6,

            })
        }


class CreateAuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = [
            'name',
            'image'
        ]
