from django import forms
from .models import Comment, Photo, Profile, User


class NewPhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['pub_date', 'user', 'comment', 'like']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['prof_pic', 'bio']

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
