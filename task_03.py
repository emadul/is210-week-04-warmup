#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A complex testcase."""

EXPENSE = 14.23
LOOKS_NICE = True
MAX_EXPENSE = 12
GET_OUT_ALIVE = False

sacrifice = (EXPENSE <= MAX_EXPENSE == GET_OUT_ALIVE ) or (EXPENSE >= MAX_EXPENSE == MAX_EXPENSE)

print sacrifice
