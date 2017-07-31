#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script Name	: global_view
# Author		: badger
# Created		: 2017/7/22
# Description	:

from XD import settings


def global_settings(request):
    STATIC_URL = settings.STATIC_URL

    PAGE_MASTER_URL = '/mis'
    PAGE_LOGIN_URL = '/mis/login'

    return locals()
