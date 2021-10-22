from django import forms

from users.models import ProfileModel


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['first_name', 'last_name', 'phone', 'email', 'country', 'state', 'postcode', 'address1', 'address2']
        exclude = ['user']