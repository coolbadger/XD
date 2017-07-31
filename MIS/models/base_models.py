#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script Name	: company_models
# Author		: badger
# Created		: 2017/7/27
# Description	: 
from django.db import models
from django.utils.translation import ugettext as _
from MIS.models.constants import *


class Author_Code(models.Model):
    group = models.IntegerField(default=1)
    name = models.CharField(max_length=50, choices=WEB_AUTHOR_TPYE)
    code = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('Author_Code')
        verbose_name_plural = _('Author_Code')


class Department(models.Model):
    name = models.CharField(max_length=500)
    desc = models.TextField()
    parent_id = models.IntegerField(null=True)
    ding_id = models.IntegerField(null=True)
    document = models.FileField(upload_to='document')

    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Department')
