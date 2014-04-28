from django import forms

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
    helper.add_input(Submit('Create', 'Create', css_class='btn-lg btn-primary'))
