from django.urls import path
from . import views

urlpatterns = [
    path('departments/', views.DepartmentsList.as_view()),
    path('departments/<int:pk>', views.DepartmentsDetail.as_view()),

    path('employees/', views.EmployeesList.as_view()),
    path('employees/<int:pk>', views.EmployeesDetail.as_view()),
]