#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script Name	: business_models
# Author		: badger
# Created		: 2017/7/27
# Description	:


# Create your models here.


from django.db import models
from django.utils.translation import ugettext as _
from MIS.models.constants import *


class Company(models.Model):
    name = models.CharField(max_length=500)
    type = models.CharField(choices=Company_Type, null=True, max_length=4, default='1')
    address = models.CharField(max_length=500, null=True, blank=True)
    corporate = models.CharField(max_length=500, null=True, blank=True)
    credit_code = models.CharField(max_length=500, null=True, blank=True)

    bank_account = models.CharField(max_length=500, null=True, blank=True)
    account_name = models.CharField(max_length=500, null=True, blank=True)
    bank_name = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Company')


class Project(models.Model):
    name = models.CharField(max_length=500)
    type = models.CharField(choices=Project_Type, max_length=4, null=True)
    detail = models.TextField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    name.verbose_name = _('Project Name')

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Project')


class Contract(models.Model):
    name = models.CharField(max_length=500)
    project = models.ForeignKey(Project)
    context = models.TextField()
    sing_date = models.DateField(null=True)

    class Meta:
        verbose_name = _('Contract')
        verbose_name_plural = _('Contract')


class Contract_Company(models.Model):
    contract = models.ForeignKey(Contract)
    company = models.ForeignKey(Company)
    role = models.CharField(choices=Contract_Company_Type, max_length=4)

    class Meta:
        verbose_name = _('Contract-Company')
        verbose_name_plural = _('Contract-Company')
