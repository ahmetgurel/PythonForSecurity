#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2

response = urllib2.urlopen('http://gurelahmet.com/')
print response.info()
response.close()
