from .models import Sub
from django import forms


class SubForm(forms.ModelForm):
    class Meta:
        model = Sub
        fields = ('sub',)


class UpvoteForm(forms.ModelForm):
    class Meta:
        model = Sub
        fields = ('user',)
