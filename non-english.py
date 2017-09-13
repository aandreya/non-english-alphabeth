#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

chars = u'@asd_ ć č đ š ž Ć Č Đ Š Ž ß Ł ł ä Ä ö Ö ü Ü ! _ 1 2 3'

ENGLISH_CHARS = re.compile('[^\W_]', re.IGNORECASE)
ALL_CHARS = re.compile('[^\W_]', re.IGNORECASE | re.UNICODE)

result_eng = ENGLISH_CHARS.findall(chars)
result_all = ALL_CHARS.findall(chars)

print('ENGLISH')
for i, char in enumerate (result_eng, 1):
    print i, char
print ('------------------')
print('ALL')
for i, char in enumerate (result_all, 1):
    print i, char