from django.shortcuts import render
from app.models import Employee
from app.serializers import EmployeeSerializer
from rest_framework import generics
from app.pagination import MyPagination
class EmployeeListView(generics.ListAPIView):
    queryset =Employee.objects.all()
    serializer_class=EmployeeSerializer
    pagination_class=MyPagination
