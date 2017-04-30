from django import forms
from .models import User as nUser
from django.contrib.auth.models import User 
class SignInForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'password']#'__all__'
    

class SignUpForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['username','email', 'password','confirm_password']#'__all__'

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

    
class SignUpFormmuser(forms.ModelForm):
    class Meta:
        model = nUser
        fields = ['bio','image']