from django.forms import forms
from ..models import subconcept


class LearnerSubconceptForm(forms.Form):
    class Meta:
        model = subconcept
        fields = ['name', 'concept']