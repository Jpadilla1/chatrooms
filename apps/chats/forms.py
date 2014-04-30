from django import forms
from django.core.validators import MinLengthValidator

from .models import ChatRoom

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CreateRoomForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ('name', 'key')
        widgets = {'key': forms.PasswordInput()}

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit(
        'Create', 'Create', css_class='btn-lg btn-primary pull-right'))


class EnrollRoomForm(forms.Form):
    key = forms.CharField(max_length=15, required=True,
                          validators=[MinLengthValidator(6), ],
                          widget=forms.PasswordInput)
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit(
        'Enroll', 'Enroll', css_class='btn-lg btn-primary pull-right'))
