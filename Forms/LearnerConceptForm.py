from django.forms import forms
from ..models import concept

class LearnerConceptForm(forms.Form):
    class Meta:
        model = concept
        fields = ['name']
