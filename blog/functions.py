#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import re
import time
import config
import string
import smtplib
import datetime
import os
import random
import Image


def pssmd5(pssaword, salt):
    mde5 = hashlib.md5()
    mde5.update(pssaword.encode("utf-8"))
    mde5.update(salt.encode("utf-8"))
    return mde5.hexdigest()
    
def validateEmail(email):
    if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
        return 1
    return None

def infodate(date, newdate,waittime):
    date= time.strptime(date)
    newdate = time.strptime(newdate)
    c=date[:5]
    d=newdate[:5]
    if c ==d:
        x= newdate[5]-date[5]
        if x > 0 and x<waittime:
            return True
            
def listtoint(mylist):
    mylist=mylist.strip()
    mylist=mylist.split(',')
    if mylist!=['']:mylist=map(int, mylist)        
    if mylist==['']:mylist=[]    
    return mylist
    
def fbuffer(raw, chunk_size=10000):
   while True:
      chunk =raw.read(chunk_size)
      if not chunk: break
      yield chunk
      
def sand(FROM,SUBJECT , TEXT, ip, email=config.TO ):
    username = config.musername
    password = config.mpassword  
    smtp= config.smtp
    TO = email 
    BODY = string.join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT ,
        "",
        TEXT, FROM, ip
        ), "\r\n")
    server = smtplib.SMTP(smtp)  
    server.starttls()  
    server.login(username,password)
    server.sendmail(FROM, [TO], BODY)
    server.quit()

def prandom(size=6, chars=string.digits+string.letters):
    return ''.join(random.choice(chars) for x in range(size))
