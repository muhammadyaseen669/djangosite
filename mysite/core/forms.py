from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'email','subject','skillset','coverletter','pdf', 'cover')
