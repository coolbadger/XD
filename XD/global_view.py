#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script Name	: global_view
# Author		: badger
# Created		: 2017/7/22
# Description	:

from XD import settings


def global_settings(request):
    STATIC_URL = settings.STATIC_URL
    return locals()
