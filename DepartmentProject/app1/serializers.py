from rest_framework.serializers import ModelSerializer

from .models import Department

class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = [
            'name',
            'location',
            'teamLead',
            'description',
            'numberOfEmployees'
        ]
