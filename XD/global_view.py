#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script Name	: global_view
# Author		: badger
# Created		: 2017/7/22
# Description	:

from XD import settings


def constants():
    STATIC_URL = settings.STATIC_URL

    PAGE_MASTER_URL = '/mis/master_page'
    PAGE_LOGIN_URL = '/mis/login'
    PAGE_LOGOUT_URL = '/mis/logout'
    return locals()


def global_settings(request):
    setting_dic = {}

    setting_dic.update(constants())
    return setting_dic
