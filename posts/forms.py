from django import forms


class AuthorForm(forms.Form):
    nick = forms.CharField(max_length=15)
    email = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')

        if '@' not in email:
            raise forms.ValidationError("Podaj poprawny imajl")


class PostForm(forms.Form):
    title = forms.CharField(max_length=50)
    content = forms.CharField(max_length=300)
    author = forms.CharField(max_length=15)
    email = forms.EmailField()

