#!/usr/bin/env python
# -*- coding: utf-8 -*-

veri = raw_input("Base64 ile Sifrelenecek Veriyi Giriniz")
sifre=veri.encode('base64','strict')
print sifre
