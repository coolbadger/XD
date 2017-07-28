#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script Name	: constants
# Author		: badger
# Created		: 2017/7/27
# Description	:
from django.utils.translation import ugettext as _

PERSON_SEX = (
    ('N', 'None'),
    ('M', 'Male'),
    ('F', 'Female'),
)

Company_Type = (
    ('1', _('Private Comp')),
    ('2', _('State-Owned Comp.')),
    ('3', _('Governmental Agencies')),
    ('4', _('Institutions')),
    ('5', _('Listed Comp.')),
    ('6', _('PLC (Public Limited Company)')),
    ('7', _('Startup Comp.')),
    ('8', _('Foreign Comp. (Eur./ N.Amerian )')),
    ('9', _('Foreign Comp. (Others)')),
    ('10', _('Joint Ventures (JV)')),
    ('11', _('Rep. (Representative) Office of Foreign Comp.')),
    ('12', _('NPO (non-profit organization)')),
    ('13', _('WFOE(Wholly Foreign Owned Enterprise)')),
)

Project_Type = (
    ('I', _('Income')),
    ('O', _('Outcome')),
)

Contract_Company_Type = (
    ('A', _('Part A')),
    ('B', _('Part B')),
    ('C', _('Part C')),
    ('D', _('Part D')),
    ('E', _('Part E')),
)
''
