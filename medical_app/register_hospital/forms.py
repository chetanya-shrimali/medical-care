from django import forms

from register_hospital.models import Hospital


class HospitalForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Hospital
        exclude = ['verification']
        # exclude['id', 'verification']


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Hospital
        fields = ['name', 'password']
