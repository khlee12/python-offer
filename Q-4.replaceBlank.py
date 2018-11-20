#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 16:25:19 2018

@author: khlee

[面试题4]
将字符串里的空格换成'%20'
"""
str1 = 'replace: blank to other string'
str2 = 'replace: multiple    blanks '
str3 = 'replace:noblanks'

print(str1.replace(' ', '%20'))
print(str2.replace(' ', '%20'))
print(str3.replace(' ', '%20'))