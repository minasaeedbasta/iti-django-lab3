
from django import forms
from authors.models import Author

class AuthorModelForm(forms.ModelForm):
    class Meta:
        model= Author
        fields='__all__'

    name = forms.CharField(label='Name' , max_length=100, help_text="Enter your name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    bdate = forms.DateField(label='Birth date' ,  widget=forms.DateInput(attrs={'class': 'form-control',"type":'date'}))
    image = forms.ImageField(label='Image',widget=forms.FileInput(attrs={'class': 'form-control'}))

    def clean_name(self):
        name= self.cleaned_data['name']
        if len(name) < 2:
             raise forms.ValidationError("Name must be at least 2 characters ")
        return name