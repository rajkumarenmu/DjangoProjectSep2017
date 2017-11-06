from django.db import models
from django.forms.models import model_to_dict, fields_for_model
import json

# Create your models here.
class Department (models.Model):

    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100, null=True)
    teamLead = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    numberOfEmployees = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    # def to_dict(self):
    #
    #     model = model_to_dict(self)
    #
    #     return model

    def to_json(self, d):

        json_output = json.dumps(d)

        return json_output

    def dict_to_obj(self, d):

        self.name = d['name']
        self.location = d['location']
        self.teamLead = d['teamLead']
        self.description = d['description']
        self.numberOfEmployees = d['numberOfEmployees']

        return self

'''
for field in fields_for_model(self):
    setattr(self, field, d[field])

return self
'''

def from_json_to_dict(j):

    output_dict = json.loads(j)

    return output_dict


class DepartmentRequestStatus(models.Model):

    status = models.CharField(max_length=100)
    departmentName = models.CharField(max_length=100)

    def to_dict(self):
        model = model_to_dict(self)

        return model




class Employee (models.Model):
    firstName = models.CharField(max_length=100, null=True)
    lastName = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstName + ' ' + self.lastName