from django import forms

from .models import Message

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CreateMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('body',)
        widgets = {'body': forms.Textarea(attrs={'cols': 80, 'rows': 5})}
        labels = {'body': 'Message'}

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Post', 'Post', css_class='btn-lg btn-primary'))
