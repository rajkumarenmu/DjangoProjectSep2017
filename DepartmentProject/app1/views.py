import json

import time
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView
from .serializers import DepartmentSerializer
from .form import DepartmentForm
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse, Http404, HttpResponseNotAllowed, HttpResponseBadRequest
from django.template import loader
from .models import Employee, Department, from_json_to_dict, DepartmentRequestStatus
from threading import Thread
# Create your views here.
def home(request):

    all_departments = Department.objects.all()
    template = loader.get_template('app1/home.html')

    data = {
        'all_departments': all_departments,
    }
    return HttpResponse(template.render(data, request))


def formView(request):

    form = DepartmentForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        if obj.name == 'Raj':
            form.save()

    data = {
        'form': form,
        'title': 'Welcome'
    }

    return render(request, 'app1/form.html', data)


def departmentIdView(request, number):

    if request.method == "HEAD":
        status = DepartmentRequestStatus.objects.get(id=number)
        if status:
            response = JsonResponse(status.to_dict(), safe=False)
            if status.status == "Pending":
                response.status_code = 202
            else:
                response.status_code = 200

            return response
    else:
        department = Department.objects.get(id = number)
        template = loader.get_template('app1/departments.html')

        data = {
            'department': department,
        }
        return HttpResponse(template.render(data, request))

def departmentApiView(request):

    if request.method == 'POST':
        body = request.body.decode('utf-8')
        data = from_json_to_dict(body)

        status = DepartmentRequestStatus()
        status.status = "Pending"
        status.departmentName = data["name"]
        status.save()

        t = Thread(target=save_department, args=(data, status))
        t.daemon = True
        t.start()

        response = JsonResponse(status.to_dict(), safe=False)
        response.status_code = 202
        return response


    elif request.method == "DELETE":
        body = request.body.decode('utf-8')
        data = json.loads(body)
        # output data = {"name": ["Health", "HR"]}
        if "name" in data:
            dept_names = data["name"]
            # output ["Health", "HR"]
            for dept_name in dept_names:
                departments = Department.objects.filter(name=dept_name)
                if len(departments) > 0:
                    for department in departments:
                        department.delete()
        else:
            return HttpResponseBadRequest()
    elif request.method == 'PUT':
        body = request.body.decode('utf-8')
        data = json.loads(body)
        if "name" in data and data["name"] is not None:
            departments = Department.objects.get(id=data["id"])
            if len(departments) > 0:
                dept = departments[0]
                dept.location = data["location"]
                dept.teamLead = data["teamLead"]
                dept.numberOfEmployees = data["numberOfEmployees"]
                dept.save()

                response = HttpResponse()
                response.status_code = 200

                return response
            else:
                raise Http404
        else:
            return HttpResponseBadRequest()
                # remaining





    else:
        response = HttpResponse()
        response.status_code = 405
        return response




def departmentApiViewByName(request, dept_name):

    if request.method == 'GET':
        departments = Department.objects.filter(name=dept_name)
        if len(departments) > 0:
            data_list = []
            for department in departments:
                data = department.to_dict()
                # json_data = department.to_json(data)
                data_list.append(data)

            response = JsonResponse(data_list, safe=False)
            response.status_code = 200
            return response
        else:
            raise Http404()

    elif request.method == "DELETE":
        departments = Department.objects.filter(name= dept_name)
        if len(departments) > 0:
            for department in departments:
                department.delete()
            response = HttpResponse()
            response.status_code = 200
            return response
        else:
            raise Http404

    else:
        response = HttpResponse()
        response.status_code = 405
        return response


def save_department(data, status):
    # for loop or time taking process

    dept = Department()
    dept.dict_to_obj(data)
    time.sleep(30)
    dept.save()
    status.status = "Completed"
    status.save()


################## REST FrameWork vies ##############

class DepartmentListAPIView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentGetAPIView(RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'dept_name'


class DepartmentDeleteAPIView(DestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'dept_name'


class DepartmentCreateAPIView(CreateAPIView):
    # POST request
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentUpdateAPIView(UpdateAPIView):
    # PUT request
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'dept_name'