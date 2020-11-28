from django import forms
from .models import Post, Profile
from django.contrib.auth.models import User

class ProfileModelForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields=('name', 'avatar', 'bio')


class NewPostForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))

    class Meta:
        model = Post
        exclude = ['user', 'post_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }        


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields=('name','bio', 'avatar')
class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'name','avatar', 'bio']
