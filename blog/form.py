from django import forms
from blog.models import User

class RegistrationForm(forms.ModelForm):
    passwd_sec = forms.PasswordInput()
    class Meta:
        model = User
        fields = ['name', 'email', 'passwd', 'is_active', '']