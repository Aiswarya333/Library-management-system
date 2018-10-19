from django import forms

from .models import Book

class BookForm(forms.ModelForm):
    title = forms.CharField(max_length=100, required=False)
    author = forms.CharField(max_length=100, required=False)
    publised_date=forms.CharField(max_length=100,required=False)
    availability=forms.CharField(max_length=100,required=False)
    class Meta:
        model = Book
        fields = ('author', 'title','publised_date','availability',)
form = BookForm()