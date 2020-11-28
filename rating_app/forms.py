from django import forms
from .models import Post, Profile

class ProfileModelForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields=('name', 'avatar', 'bio')


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'post_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }        

