from django import forms
from django.forms import ModelForm

from .models import Comment,Contact



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')



class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

