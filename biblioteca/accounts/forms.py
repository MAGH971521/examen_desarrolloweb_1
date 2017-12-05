from django import forms


class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={'placeholder': "Username*", 'class': "input"}))
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(
            attrs={'placeholder': "chris@email.com*", 'class': "input"}))
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={'placeholder': "Password*", 'class': "input"}))
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={'placeholder': "Password2*", 'class': "input"}))

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("La claves deben ser iguales!")
        return password2
