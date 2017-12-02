from django import forms

from register_hospital.models import Hospital


class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        exclude = ['verification']
        # exclude['id', 'verification']
