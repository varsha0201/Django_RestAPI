# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employees
from .serialize import employeesSerializer

class employeeList(APIView):

    def get(self, request):
        employees1 = employees.objects.all()
        serialize = employeesSerializer(employees1, many=True)
        return Response(serialize.data)

    def post(self):
        pass