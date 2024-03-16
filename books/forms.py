
from django import forms
from books.models import Book

class BookModelForm(forms.ModelForm):
    class Meta:
        model= Book
        fields='__all__'

    name = forms.CharField(label='Name' , max_length=100, help_text="Enter your name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(label='Image',widget=forms.FileInput(attrs={'class': 'form-control'}))

    def clean_name(self):
        name= self.cleaned_data['name']
        if len(name) < 2:
             raise forms.ValidationError("Name must be at least 2 characters ")
        return name