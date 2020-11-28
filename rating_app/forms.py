from django import forms
from .models import Post, Profile


class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    class Meta:
        model= Post
        fields=('content', 'image' )


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields=('first_name', 'last_name', 'bio', 'avatar')