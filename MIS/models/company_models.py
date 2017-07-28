#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script Name	: company_models
# Author		: badger
# Created		: 2017/7/27
# Description	: 
from django.db import models
from django.utils.translation import ugettext as _
from MIS.models import business_models
from MIS.models.constants import *


class Department(models.Model):
    name = models.CharField(max_length=500)
    campany = models.ForeignKey(business_models.Company)
    document = models.FileField(upload_to='document')

    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Department')


class Person(models.Model):
    name = models.CharField(max_length=500, help_text="Input your name")
    sex = models.CharField(max_length=4, choices=PERSON_SEX, default='M')
    info = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('Person')
