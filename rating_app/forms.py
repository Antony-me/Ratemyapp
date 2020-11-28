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


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'name','avatar', 'bio']
