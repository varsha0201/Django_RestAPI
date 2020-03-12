# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.
class employees(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    emp_id = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return self.firstname

