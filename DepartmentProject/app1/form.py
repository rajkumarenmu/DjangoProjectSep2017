from django import forms

from .models import Department

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name',
            'location',
            'teamLead',
            'description',
            'numberOfEmployees'
        ]

    def validate_form(self):
