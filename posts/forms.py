from django import forms

from posts.models import Post, Author


class AuthorForm(forms.Form):
    nick = forms.CharField(max_length=15)
    email = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')

        if '@' not in email:
            raise forms.ValidationError("Podaj poprawny imajl")


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "author"]

"""
class AuthorForm(forms.ModelForm):
    class Meta:
        model: Author
        fields: '__all__'
"""