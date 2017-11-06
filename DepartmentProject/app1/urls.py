from django.conf.urls import include, url
from app1.views import *
urlpatterns = [
    # Examples:
    # url(r'^$', 'NewProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^home/$', home),
    url(r'^departments/(?P<number>[0-9])/$', departmentIdView),
    url(r'^departmentsApi/$', departmentApiView),
    url(r'^departmentsApi/(?P<dept_name>[a-zA-Z]+)/$', departmentApiViewByName),
    url(r'^departmentsRestApi/$', DepartmentListAPIView.as_view()),
    url(r'^departmentsRestApi/(?P<dept_name>[\w-]+)/$', DepartmentGetAPIView.as_view()),
    url(r'^departmentsRestApi/delete/(?P<dept_name>[\w-]+)/$', DepartmentDeleteAPIView.as_view()),
    url(r'^departmentsRestApiCreate/$', DepartmentCreateAPIView.as_view()),
    url(r'^departmentsRestApiUpdate/(?P<dept_name>[\w-]+)/$', DepartmentUpdateAPIView.as_view()),
    url(r'^departmentsFormView/$', formView),



]