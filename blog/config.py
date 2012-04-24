#!/usr/bin/env python
# -*- coding: utf-8 -*-

import CaptchasDotNet

######sql######
host='localhost'
username='root'
passdb=''
namedb=''

######mail######
musername = 'sultan4ksa@gmail.com'  
mpassword = ''  
smtp='smtp.gmail.com:587'
TO = 'sultan4ksa@gmail.com'

#####cookie#####
secretkey=''

#####captchas#####
#http://captchas.net/
captchas = CaptchasDotNet.CaptchasDotNet (client   = 'demo',secret   = 'secret',
                                alphabet = 'abcdefghkmnopqrstuvwxyz',
                                letters  = 4,
                                width    = 110,
                                height   = 70
                                )
