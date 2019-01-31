from rest_framework import serializers
from .models import Departments, Employees


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('name', 'code', 'position')


class DepartmentsSerializer(serializers.ModelSerializer):
    employees = EmployeesSerializer(many=True, read_only=True)

    class Meta:
        model = Departments
        fields = ('id', 'title', 'employees')
