#!/usr/bin/env python
# -*- coding: utf-8 -*-


veri = raw_input("Base64 ile Sifrelenecek Veriyi Giriniz:")
salt="qwey123"
salt_veri=veri+salt
sifre=salt_veri.encode('base64','strict')
print sifre
