from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='User name')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class EmailLoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class MemoryLoginForm(forms.Form):
    username = forms.CharField(label='User name')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    memory = forms.BooleanField(label='Remember user', required=False)


USER_TYPES = ['Student', 'teacher', 'admin']


class UserTypesLoginForm(forms.Form):
    username = forms.CharField(label='User name')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    user_type = forms.ChoiceField(label='User type', choices=USER_TYPES)
