#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
LightBlog is simple Blog in Python language and Easy development Because it uses a bottle framework..
Homepage : http://lightscr.net
Email : sultan4ksa@gmail.com
Copyright (c) 2012, Sultan Alenazi.
License: MIT (see LICENSE for details)
"""
__author__ = 'Sultan Alenazi'
__version__ = '1.1.0'
__license__ = 'MIT'

from bottle import route, run, post, request, response, template, debug, static_file, redirect, error, abort
import bottle
from model import  newuser, userstable,editusers,deleteuser, lenuser, infoall, infofetchall, newblog, infoblog, infoblogall \
, newcomment, infocomments , lenblog, deleteblog, editblog, editcomment, deletecomment, infocommentall \
, newsection, editsection, deletesection, infosection, infoblogsection, lenblogsection,ifsection,  infovalid,infovalids,  editvalid,infosite, editsite, infoblogip\
,infocommentip,infoblogmap, editusersnopass, editusercp, editusercppass, addblog2comm,delblog2comm, infoother, editother,editpass2, updateuser, updateemail\
, infoblogtag, lenblogtag, iftag, infoblogsearch, lenblogsearch, ifsearch

import CaptchasDotNet
from cgi import escape as xss
from MySQLdb import escape_string as xsql
import config
from datetime import datetime, date
import os, sys
import random
import string
from functions import pssmd5,validateEmail, infodate, listtoint, fbuffer, sand, prandom
from shutil import copy2


try:
    import PyRSS2Gen
    from postmarkup import strip_bbcode
except ImportError:
    pass

##########set config
secretkey=config.secretkey
captchas = config.captchas

##########global 
other=infoother()
cookie_age=other[1].encode("utf8")
waittime=other[2]
sizeupload=other[3]
numblog=other[4]
numcomment=other[5]
style=other[6]
styleadmin=other[7]
language=other[8]
avatorwidth= other[9]
avatorheight= other[10]

valids=infovalids()
validblognew=valids[1] 
validcommen=valids[2]
validadmin=valids[3]
valideditusers=valids[4]
validblogedit=valids[5]
validcommentedit=valids[6]

infomysite=infosite()
modsite=infomysite[6]
modmsg=infomysite[7]

##########import language
try:
    exec('import languages.%s')%language
    exec('lang=languages.%s.lang')%language
except ImportError:
    import languages.en
    lang=languages.en.lang

########## blog code
@route('/blog')
def rblog():
    redirect("/blog/")

@route('/')
@route('/<page:int>')
@route('/blog/')
@route('/blog/<page:int>')
def blog(loginstat='', page=1):
    username=infousername=request.get_cookie("account", secret=secretkey)
    if not modsite:
        return template('styles/'+style+'/template/info', title=lang['info'],infousername=infousername, text=modmsg , site=infomysite)
    next,back,ends=page+1, page-1, numblog
    start= (page- 1) * ends
    blogs=list(infoblogall(start, ends))
    lblog=int(lenblog())
    lend=(page*numblog)-numblog
    site=infomysite
    title=site[1]
    keywords=site[2]
    description=site[3]
    url=''
    if username:
        return template('styles/'+style+'/template/blog',title=title, keywords=keywords, description=description,url=url,lblog=lblog,lend=lend, next=next,back=back,  page=page , loginstat='', username=username, blogs=blogs,  infousername=infousername, rposts=infocommentall(numcomment),  allsection=infosection(), site=site, alert='', noblog=lang['''No blog'''])
    return template('styles/'+style+'/template/blog',title=title, keywords=keywords, description=description,url=url,lblog=lblog, lend=lend,next=next ,back=back, page=page , loginstat=loginstat, username=username, blogs=blogs, infousername=infousername, rposts=infocommentall(numcomment), allsection= infosection(), site=site, alert='', noblog=lang['''No blog'''])

@route('/section/<section>')
@route('/section/<section>/<page:int>')
@route('/blog/section/<section>')
@route('/blog/section/<section>/<page:int>')
def sectionblog(section,loginstat='', page=1):
    username=infousername=request.get_cookie("account", secret=secretkey)
    if not modsite:
        return template('styles/'+style+'/template/info', title=lang['info'],infousername=infousername, text=modmsg, site=infomysite)
    section=xsql(xss(section.replace('-',' ')))
    next,back,ends=page+1, page-1,numblog
    start= (page- 1) * ends
    blogs=list(infoblogsection(section, start,ends))
    lblog=int(lenblogsection(section))
    mysection=ifsection(section)    
    if not mysection:
        return template('styles/'+style+'/template/info', title=lang['error'],infousername=infousername, text=lang['''You haven't chosen a section'''], site=infomysite)
    lend=(page*numblog)-numblog
    site=infomysite
    title=section+' - '+site[1].encode("utf8")
    keywords=mysection[0][2]
    description=mysection[0][3]
    url='''section/%s/'''%(section.replace(' ','-'))
    if username:
        return template('styles/'+style+'/template/blog',title=title, keywords=keywords, description=description, url=url, lblog=lblog,lend=lend, next=next,back=back,  page=page , loginstat='', username=username, blogs=blogs,  infousername=infousername, rposts=infocommentall(numcomment), allsection=infosection(), site=site, alert=lang['''Category Archives: '%s' ''']%section, noblog=lang['''No blog'''])
    return template('styles/'+style+'/template/blog',title=title, keywords=keywords, description=description,url=url, lblog=lblog, lend=lend,next=next ,back=back, page=page , loginstat=loginstat,username=username, blogs=blogs,infousername=infousername, rposts=infocommentall(numcomment), allsection= infosection(), site=site, alert=lang['''Category Archives: '%s' ''']%section, noblog=lang['''No blog'''])

@route('/tag/<tag>')
@route('/tag/<tag>/<page:int>')
@route('/blog/tag/<tag>')
@route('/blog/tag/<tag>/<page:int>')
def tagblog(tag,loginstat='', page=1):
    username=infousername=request.get_cookie("account", secret=secretkey)
    if not modsite:
        return template('styles/'+style+'/template/info', title=lang['info'],infousername=infousername, text=modmsg, site=infomysite)
    tag=xsql(xss(tag.replace('-',' ')))
    next,back,ends=page+1, page-1,numblog
    start= (page- 1) * ends
    blogs=list(infoblogtag(tag, start,ends))
    lblog=int(lenblogtag(tag))
    mytag=iftag(tag)
    if len(tag)<3:
        return template('styles/'+style+'/template/info', title='error',infousername=infousername, text=lang['''Number of characters is less than 3'''], site=infomysite)
    lend=(page*numblog)-numblog
    site=infomysite
    title=tag+' - '+site[1].encode("utf8")
    keywords=tag
    description=tag
    url='''tag/%s/'''%(tag.replace(' ','-'))
    if username:
        return template('styles/'+style+'/template/blog',title=title, keywords=keywords, description=description,url=url, lblog=lblog,lend=lend, next=next,back=back,  page=page , loginstat='', username=username, blogs=blogs,  infousername=infousername, rposts=infocommentall(numcomment), allsection=infosection(), site=site, alert=lang['''Tag Archives: '%s' ''']%tag, noblog=lang['''No blog'''])
    return template('styles/'+style+'/template/blog',title=title, keywords=keywords, description=description,url=url, lblog=lblog, lend=lend,next=next ,back=back, page=page , loginstat=loginstat,username=username, blogs=blogs,infousername=infousername, rposts=infocommentall(numcomment),allsection= infosection(), site=site, alert=lang['''Tag Archives: '%s' ''']%tag, noblog=lang['''No blog'''])

@route('/search/<search>')
@route('/search/<search>/<page:int>')
@route('/blog/search/<search>')
@route('/blog/search/<search>/<page:int>')
def searchblog(search,loginstat='', page=1):
    username=infousername=request.get_cookie("account", secret=secretkey)
    if not modsite:
        return template('styles/'+style+'/template/info', title=lang['info'],infousername=infousername, text=modmsg, site=infomysite)
    search=xsql(xss(search.replace('-',' ')))
    next,back,ends=page+1, page-1,numblog
    start= (page- 1) * ends
    blogs=list(infoblogsearch(search, start,ends))
    lblog=int(lenblogsearch(search))
    mysearch=ifsearch(search)
    if len(search)<3:
        return template('styles/'+style+'/template/info', title='error',infousername=infousername, text=lang['''Number of characters is less than 3'''], site=infomysite)
    lend=(page*numblog)-numblog
    site=infomysite
    title=search+' - '+site[1].encode("utf8")
    keywords=search
    description=search
    url='''search/%s/'''%(search.replace(' ','-'))
    if username:
        return template('styles/'+style+'/template/blog',title=title, keywords=keywords, description=description,url=url,lblog=lblog,lend=lend, next=next,back=back,  page=page , loginstat='', username=username, blogs=blogs,  infousername=infousername, rposts=infocommentall(numcomment) , allsection=infosection(), site=site, alert=lang['''Search Results for: '%s' ''']%search, noblog=lang['''No blog'''])
    return template('styles/'+style+'/template/blog',title=title, keywords=keywords, description=description,url=url,lblog=lblog, lend=lend,next=next ,back=back, page=page , loginstat=loginstat,username=username, blogs=blogs,infousername=infousername, rposts=infocommentall(numcomment),allsection= infosection(), site=site, alert=lang['''Search Results for: '%s' ''']%search, noblog=lang['''No blog'''])

@post('/search')
@post('/blog/search')
def search():    
    search=request.forms.get('search')
    redirect("/blog/search/%s"%search.replace(' ','-'))
    
@post('/login')
@post('/blog/login')
def login_submit():
    username=unicode(xsql(xss(request.forms.get('username'))), encoding='utf-8')
    password= unicode(xsql(xss(request.forms.get('password'))), encoding='utf-8')
    box= request.forms.get('box')
    row=infofetchall('username',username)
    if row:
        salt=row[0][10]
        password=pssmd5(password,salt)
        if row[0][1]==username and row[0][2]==password or row[0][9]==password:
            validuser=str(row[0][6])
            if box:
                response.set_cookie("account",username, secret=secretkey)
                response.set_cookie("validuser",validuser, secret=secretkey)
            else:
                response.set_cookie("account",username,secret=secretkey, max_age=cookie_age)
                response.set_cookie("validuser",validuser,secret=secretkey, max_age=cookie_age)
            redirect("/blog/")
    return blog(lang['''Login Error! <a  href='/blog/rpassword'>Recover Lost Password</a>'''])

@route('/signout')
@route('/blog/signout')
def login_out():
    username=request.get_cookie("account", secret=secretkey)
    validuser=request.get_cookie("validuser", secret=secretkey)
    response.delete_cookie("account")
    response.delete_cookie("validuser")
    return '''<META HTTP-EQUIV="Refresh" CONTENT="0;URL=/blog/">'''

@route('/rpassword')
@route('/blog/rpassword')
def rpassword_form():
    infousername=request.get_cookie("account", secret=secretkey)
    if not modsite:
        return template('styles/'+style+'/template/info', title=lang['info'],infousername=infousername, text=modmsg, site=infomysite)
    return template('styles/'+style+'/template/rpassword',error='', infousername=infousername, random=captchas.random (), image=captchas.image (), audio_url=captchas.audio_url (), site=infomysite)

@post('/rpassword')
@post('/blog/rpassword')
def rpassword_submit():
    infousername=request.get_cookie("account", secret=secretkey)
    if not modsite:
        return template('styles/'+style+'/template/info', title=lang['info'],infousername=infousername, text=modmsg, site=infomysite)
    email= xsql(xss(request.forms.get('email')))
    capt= xss(request.forms.get('capt'))
    ip = request.get('REMOTE_ADDR')
    password2=prandom(8)
    FROM=config.TO
    SUBJECT=lang['Recover Lost Password']
    TEXT=lang['hi \n the new password is %s']%password2
    row=infofetchall('email',email)
    if not captchas.verify (capt):
        return template('styles/'+style+'/template/rpassword',error=lang["CAPTCHA input isn't valid."], infousername=infousername, random=captchas.random (), image=captchas.image (), audio_url=captchas.audio_url (), site=infomysite)
    if not row:
        return template('styles/'+style+'/template/rpassword',error=lang["Error email"], infousername=infousername, random=captchas.random (), image=captchas.image (), audio_url=captchas.audio_url (), site=infomysite)
    salt=row[0][10]
    password2=pssmd5(password2,salt)
    editpass2(password2, email)
    sand(FROM,SUBJECT ,TEXT, ip, email)
    return template('styles/'+style+'/template/info', title='infomail',infousername=infousername, text=lang['''password was sent successfully'''], site=infomysite)

@route('/register')
@route('/blog/register')
def register_form():
    infousername=request.get_cookie("account", secret=secretkey)
    if not modsite:
        return template('styles/'+style+'/template/info', title=lang['info'],infousername=infousername, text=modmsg, site=infomysite)
    return template('styles/'+style+'/template/register',infousername=infousername, error='', random=captchas.random (), image=captchas.image (), audio_url=captchas.audio_url (), site=infomysite)

@post('/register')
@post('/blog/register')
def register_submit():
    infousername=request.get_cookie("account", secret=secretkey)
    if not modsite:
        return template('styles/'+style+'/template/info', title=lang['info'],infousername=infousername, text=modmsg, site=infomysite)
    username= unicode(xsql(xss(request.forms.get('username'))), encoding='utf-8')
    password= unicode(xsql(xss(request.forms.get('password'))), encoding='utf-8')
    password2= unicode(xsql(xss(request.forms.get('password2'))), encoding='utf-8')
    email= unicode(xsql(xss(request.forms.get('email'))), encoding='utf-8')
    capt= xss(request.forms.get('capt'))
    ip = request.get('REMOTE_ADDR')
    if not captchas.verify (capt):
        return template('styles/'+style+'/template/register',infousername=infousername,error=lang["CAPTCHA input isn't valid."], random=captchas.random (), image=captchas.image (), audio_url=captchas.audio_url (), site=infomysite)
    if  username=='' or password=='' or email=='':
        return template('styles/'+style+'/template/register',infousername=infousername,error=lang["Please Enter a (username, password ,email)"], random=captchas.random (), image=captchas.image (), audio_url=captchas.audio_url (), site=infomysite)
    if username[0]==' ':
        return template('styles/'+style+'/template/register',infousername=infousername,error=lang['Username must not begin with a space'], random=captchas.random (), image=captchas.image (), audio_url=captchas.audio_url (), site=infomysite)
    if not password==password2:
        return template('styles/'+style+'/template/register',infousername=infousername,error=lang["Passwords must match"], random=captchas.random (), image=captchas.image (), audio_url=captchas.audio_url (), site=infomysite)
    if not validateEmail(email):
        return template('styles/'+style+'/template/register',infousername=infousername,error=lang["Error email"], random=captchas.random (), image=captchas.image (), audio_url=captchas.audio_url (), site=infomysite)
    if infoall('username', username):
        return template('styles/'+style+'/template/register',infousername=infousername,error=lang["username  isn't available"], random=captchas.random (), image=captchas.image (), audio_url=captchas.audio_url (), site=infomysite)
    if infoall('email', email):
        return template('styles/'+style+'/template/register',error=lang["the email isn't available"], random=captchas.random (), image=captchas.image (), audio_url=captchas.audio_url (), site=infomysite)
    salt=prandom()
    password=pssmd5(password, salt)
    date=datetime.now().ctime()
    id=newuser(username,password, email, ip, date, salt)
    dirs=os.path.dirname(__file__)+'/avator/'
    avator=str(id)
    copy2(dirs+'0'+'.jpeg', dirs+avator+'.jpeg')
    return template('styles/'+style+'/template/info', title=lang['Welcome'],infousername=infousername, text=lang['''You have been successfully registered'''], site=infomysite)

@route('/new')
@route('/blog/new')
def new_form():
    username =infousername=request.get_cookie("account", secret=secretkey)
    if not modsite:
        return template('styles/'+style+'/template/info', title=lang['info'],infousername=infousername, text=modmsg, site=infomysite)
    validuser=request.get_cookie("validuser", secret=secretkey)
    if username:
        if int(validuser) in listtoint(validblognew):
            return template('styles/'+style+'/template/new', username=True,infousername=infousername,sections=infosection(), error='', site=infomysite)
        return template('styles/'+style+'/template/info', title=lang['error'],infousername=infousername, text=lang['''The page can't be viewed'''], site=infomysite)
    return template('styles/'+style+'/template/new', username=None,infousername=infousername,error=lang["Please loginPlease login username <br><a  href='/blog'>return login page</a>"], site=infomysite)

@post('/new')
@post('/blog/new')
def new_submit():
    username=infousername=request.get_cookie("account", secret=secretkey)
    if not modsite:
        return template('styles/'+style+'/template/info', title=lang['info'],infousername=infousername, text=modmsg, site=infomysite)
    validuser=request.get_cookie("validuser", secret=secretkey)
    title= unicode(xsql(xss(request.forms.get('title'))), encoding='utf-8')
    titletext= unicode(xsql(request.forms.get('titletext')), encoding='utf-8')
    section= unicode(xsql(xss(request.forms.get('section'))), encoding='utf-8')
    keywords= unicode(xsql(xss(request.forms.get('keywords'))), encoding='utf-8')
    description= unicode(xsql(xss(request.forms.get('description'))), encoding='utf-8')
    ip = request.get('REMOTE_ADDR')
    newdate=datetime.now().ctime()
    if title=='' or  titletext=='' or titletext=='<br>':
        return template('styles/'+style+'/template/info', title=lang['error'],infousername=infousername, text=lang['''You haven't filled the title or the blog field'''], site=infomysite)
    if not keywords: keywords=title.strip().replace(' ',',')
    if not description:
        try:
            description=strip_bbcode(titletext[:200])
        except NameError:
            description=titletext[:200]
    if username:
        if int(validuser) in listtoint(validblognew):
            date=infoblogip(ip)
            if date:
                if infodate(date, newdate,waittime):
                    return template('styles/'+style+'/template/info', title=lang['error'],infousername=infousername, text=lang['Please wait %s second/s']%waittime, site=infomysite)
            id=newblog(username,title,titletext, section, keywords, description, ip, date=newdate)
            return '''<META HTTP-EQUIV="Refresh" CONTENT="0;URL=/blog/comment/%d">'''%id
        return template('styles/'+style+'/template/info', title=lang['error'],infousername=infousername, text=lang['''The page can't be viewed'''], site=infomysite)

@route('/sand')
@route('/blog/sand')
def sand_mail():
    infousername=request.get_cookie("account", secret=secretkey)
    return template('styles/'+style+'/template/sand',error='', infousername=infousername, random=captchas.random (), image=captchas.image (), audio_url=captchas.audio_url (), site=infomysite)
    
@post('/sand')
@post('/blog/sand')
def sand_submit():
    infousername=request.get_cookie("account", secret=secretkey)
    FROM= xss(request.forms.get('FROM'))
    SUBJECT= xss(request.forms.get('SUBJECT'))
    TEXT= xss(request.forms.get('TEXT'))
    capt= xss(request.forms.get('capt'))
    ip = request.get('REMOTE_ADDR')
    if not captchas.verify (capt):
        return template('styles/'+style+'/template/sand',error=lang["CAPTCHA input isn't valid."],infousername=infousername, random=captchas.random (), image=captchas.image (), audio_url=captchas.audio_url (), site=infomysite)
    if  FROM=='' or SUBJECT=='' or TEXT=='':
        return template('styles/'+style+'/template/sand',error=lang["Please enter (YOUREMAIL, SUBJECT, MESSAGE)"],infousername=infousername, random=captchas.random (), image=captchas.image (), audio_url=captchas.audio_url (), site=infomysite)
    sand(FROM,SUBJECT , TEXT, ip)
    return template('styles/'+style+'/template/info', title='infomail',infousername=infousername, text=lang['''Email has been sent successfully'''], site=infomysite)

@route('/comment/<id:int>')
@route('/blog/comment/<id:int>')
def blog_id(id):
    infousername=request.get_cookie("account", secret=secretkey)
    if not modsite:
        return template('styles/'+style+'/template/info', title=lang['info'],infousername=infousername, text=modmsg, site=infomysite)
    validuser=request.get_cookie("validuser", secret=secretkey)
    blog=infoblog(id)
    comments=infocomments(id)
    onvalidcommen=None
    if blog:
        signatureblog=infofetchall('username', blog[1])[0]
        if infousername:
            if int(validuser) in listtoint(validcommen):
                onvalidcommen=True
                return template('styles/'+style+'/template/comment', page=id,blog=blog,  comments=comments ,  infousername=infousername, allsection=infosection(), validcommen=validcommen, onvalidcommen=onvalidcommen,signatureblog=signatureblog, rposts=infocommentall(numcomment), site=infomysite)
            return template('styles/'+style+'/template/comment',page=id,blog=blog, comments=comments,infousername=infousername, allsection=infosection(), validcommen=validcommen, onvalidcommen=onvalidcommen,signatureblog=signatureblog, rposts=infocommentall(numcomment),site=infomysite)
        return template('styles/'+style+'/template/comment',page=id,blog=blog,comments=comments , infousername=infousername, allsection=infosection(),validcommen=validcommen, onvalidcommen=onvalidcommen,signatureblog=signatureblog, rposts=infocommentall(numcomment), site=infomysite)
    return template('styles/'+style+'/template/info', title=lang['error'],infousername=infousername, text=lang['Please, enter a correct ID'], site=infomysite)
    
@post('/comment/sandcomment/<page:int>')
@post('/blog/comment/sandcomment/<page:int>')
def comment_submit(page):
    infousername=request.get_cookie("account", secret=secretkey)
    if not modsite:
        return template('styles/'+style+'/template/info', title=lang['info'],infousername=infousername, text=modmsg, site=infomysite)
    validuser=request.get_cookie("validuser", secret=secretkey)
    if infousername:
        name=infousername
        infoyourname=infofetchall('username', infousername)[0]
        email=infoyourname[3]
        avator=infoyourname[7]
    else:
        name=unicode(xsql(xss(request.forms.get('name'))), encoding='utf-8')
        email=unicode(xsql(xss(request.forms.get('email'))), encoding='utf-8')
        avator='0'
    post=unicode(xsql(xss(request.forms.get('post'))), encoding='utf-8')
    ip = request.get('REMOTE_ADDR')
    newdate=datetime.now().ctime()
    if name!=''and page!='' and email !='' and post!='':
        if name[0]==' ':
            return template('styles/'+style+'/template/info', title=lang['error'],infousername=infousername, text=lang['Username must not begin with a space'], site=infomysite)
        if not infousername:
            if infoall('username', name):
                return template('styles/'+style+'/template/info', title=lang['error'],infousername=infousername, text=lang['Username reserved'], site=infomysite)
            if not validateEmail(email):
                return template('styles/'+style+'/template/info', title=lang['error'],infousername=infousername, text=lang['''Email isn't correct'''], site=infomysite)
        if validcommen:
            if int(validuser) in listtoint(validcommen):
                date=infocommentip(ip)
                if date:
                    if infodate(date, newdate,waittime):
                        return template('styles/'+style+'/template/info', title=lang['error'],infousername=infousername, text=lang['Please wait %s second/s']%waittime, site=infomysite)
                id=newcomment(name,page,email, post, ip,avator,date=newdate)
                addblog2comm(page)
                return '''<META HTTP-EQUIV="Refresh" CONTENT="0;URL=/blog/comment/%d#post%d">'''%(page, id)
            return template('styles/'+style+'/template/info', title=lang['error'],infousername=infousername, text=lang['''The page can't be viewed'''], site=infomysite)
        date=infocommentip(ip)
        if date:
            if infodate(date, newdate,waittime):
                return template('styles/'+style+'/template/info', title=lang['error'],infousername=infousername, text=lang['Please wait %s second/s']%waittime, site=infomysite)
        id=newcomment(name,page,email, post, ip,avator, date=newdate)
        addblog2comm(page)
        return '''<META HTTP-EQUIV="Refresh" CONTENT="0;URL=/blog/comment/%d#post%d">'''%(page, id)
    return template('styles/'+style+'/template/info', title=lang['error'],infousername=infousername, text=lang['Did not enter all fields'], site=infomysite)

@route('/usercp')
@route('/blog/usercp')
def usercp():
    infousername=request.get_cookie("account", secret=secretkey)
    if not modsite:
        return template('styles/'+style+'/template/info', title=lang['info'],infousername=infousername, text=modmsg, site=infomysite)
    if infousername:
        infouser=infofetchall('username', infousername)[0]
        return template('styles/'+style+'/template/usercp',error='', infousername=infousername,infouser=infouser,site=infomysite)
    return template('styles/'+style+'/template/info', title=lang['error'],infousername=infousername, text=lang['''The page can't be viewed'''], site=infomysite)
    
@post('/usercp')
@post('/blog/usercp')
def usercp_submit():
    infousername=username=request.get_cookie("account", secret=secretkey)
    if not modsite:
        return template('styles/'+style+'/template/info', title=lang['info'],infousername=infousername, text=modmsg, site=infomysite)
    password=unicode(xsql(xss(request.forms.get('password'))), encoding='utf-8')
    rpassword=unicode(xsql(xss(request.forms.get('rpassword'))), encoding='utf-8')
    email=unicode(xsql(xss(request.forms.get('email'))), encoding='utf-8')
    signature=unicode(xsql(xss(request.forms.get('signature'))), encoding='utf-8')
    if infousername:
        infouser=infofetchall('username', infousername)[0]
        if password:
            if password==rpassword:
                salt=prandom()
                password=pssmd5(password,salt)
                editusercppass(password, email, signature, username, salt)
                return template('styles/'+style+'/template/usercp',error=lang['Information has been saved'], infousername=infousername,infouser=infouser,site=infomysite)
            else:
                return template('styles/'+style+'/template/usercp',error=lang["Passwords must match"], infousername=infousername,infouser=infouser,site=infomysite)
        else:
            editusercp(email, signature, username)
            return template('styles/'+style+'/template/usercp',error=lang['Information has been saved'], infousername=infousername,infouser=infouser,site=infomysite)

@post('/usercp/pic')
@post('/blog/usercp/pic')
def usercp_pic():
    username=infousername=request.get_cookie("account", secret=secretkey)
    if not modsite:
        return template('styles/'+style+'/template/info', title=lang['info'],infousername=infousername, text=modmsg, site=infomysite)
    if infousername:
        try: # Windows needs stdio set for binary mode.
            from msvcrt import setmode
            setmode (0, os.O_BINARY) # stdin  = 0
            setmode (1, os.O_BINARY) # stdout = 1
        except ImportError:
            pass
        username=infofetchall('username', username)[0]
        idusername=username[0]
        infopicture=username[7]
        picture= request.files.get('picture')
        if picture !=None:
            raw = picture.file 
            filename = picture.filename.lower()
            if filename.endswith(('jpg', 'gif', 'png', 'bmp')):
                end=filename[-3:]
            elif filename.endswith('jpeg'):
                end=filename[-4:]
            else:
                return template('styles/'+style+'/template/info', title=lang['error'],infousername=infousername, text=lang['Extension is allowed, permitted extensions (jpg, gif, png, bmp, jpeg)'], site=infomysite)
            dirs=os.path.dirname(__file__)+'/avator/'
            avator=str(idusername)+'.'+end 
            logfile = file(dirs+avator, 'wb')
            for chunk in fbuffer(raw):
                logfile.write(chunk)   
            logfile.close()
            sizefile=(int(os.path.getsize(dirs+avator))/1024)
            if sizefile>sizeupload:
                os.remove(dirs+avator)
                return template('styles/'+style+'/template/info', title=lang['error'],infousername=infousername, text=lang['Size is not allowed, you must be the size is less than 2 MB'], site=infomysite)
            try:
                import Image
                imin = Image.open(dirs+avator)
                imout = imin.resize((avatorwidth, avatorheight), Image.BICUBIC) 
                os.remove('avator/'+avator)
                avator=str(idusername)+'.jpeg'
                imout.convert('RGB').save(dirs+avator)
            except ImportError:
                if end!='jpeg':
                    os.remove('avator/'+avator)
                    return template('styles/'+style+'/template/info', title=lang['error'],infousername=infousername, text=lang['Extension is allowed, permitted extensions (jpeg)'], site=infomysite)
                else:
                    pass
            except NameError:
                pass
            except  IOError:
                os.remove('avator/'+avator)
                return template('styles/'+style+'/template/info', title=lang['info'],infousername=infousername, text=lang['''avator isn't correct'''], site=infomysite)
            return template('styles/'+style+'/template/info', title=lang['info'],infousername=infousername, text=lang['avator has been saved successfully'], site=infomysite)
        return template('styles/'+style+'/template/info', title=lang['error'],infousername=infousername, text=lang['Did not choose a avator'], site=infomysite)

@route('/rss')
@route('/rss.xml')
@route('/blog/rss')
@route('/blog/rss.xml')
def rss():
    infousername=request.get_cookie("account", secret=secretkey)
    if not modsite:
        return template('styles/'+style+'/template/info', title=lang['info'],infousername=infousername, text=modmsg, site=infomysite)
    blog=infoblogall(0, 10)
    lblog=len(blog)
    try:
        rss= PyRSS2Gen.RSS2(title = infomysite[1],link = infomysite[5], description = infomysite[3])
        for i in range(0, lblog):
            rss.items.append(PyRSS2Gen.RSSItem(title = blog[i][2],link ='http://%s/blog/comment/%s'%(infomysite[5], blog[i][0]),description = blog[i][7]))
        response.content_type = 'text/xml; charset=UTF-8' 
        return  rss.to_xml("utf-8")
    except NameError:
        pass
    
@route('/sitemap')
@route('/blog/sitemap')
def sitemap():
    infousername=request.get_cookie("account", secret=secretkey)
    if not modsite:
        return template('styles/'+style+'/template/info', title=lang['info'],infousername=infousername, text=modmsg, site=infomysite)
    section=infosection()
    blog=infoblogmap()
    return template('styles/'+styleadmin+'/template/sitemap', section=section,blog=blog,site=infomysite )

@route('sitemap.xml')
@route('/blog/sitemap.xml')
def sitemapxml():
    infousername=request.get_cookie("account", secret=secretkey)
    if not modsite:
        return template('styles/'+style+'/template/info', title=lang['info'],infousername=infousername, text=modmsg, site=infomysite)
    response.content_type = 'text/xsl; charset=UTF-8' 
    return template('styles/'+styleadmin+'/template/sitemapxml', section=infosection(),blog=infoblogmap(),today=date.today(), site=infomysite )

###########admin code

@route('/header')
@route('/blog/header')
def header():
    return template('styles/'+styleadmin+'/template/header')

@route('/lftframe')
@route('/blog/lftframe')
def lftframe():
    return template('styles/'+styleadmin+'/template/lftframe')
    
@route('/admin')
@route('/blog/admin')
def admin():
    username = request.get_cookie("account", secret=secretkey)
    validuser=request.get_cookie("validuser", secret=secretkey)
    if username:
        if int(validuser) in listtoint(validadmin):
            return template('styles/'+styleadmin+'/template/mainfile')
        return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["You do not have administrative powers"])
    return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["Please login username <br><a  href='/blog'>return login page</a>"])

@route('/admin/welcome')
@route('/blog/admin/welcome')
def welcome():
    username = request.get_cookie("account", secret=secretkey)
    validuser=request.get_cookie("validuser", secret=secretkey)
    if username:
        if int(validuser) in listtoint(validadmin):
            return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["Welcome Login %s"]%username.encode("utf8"))
    return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["Please login username <br><a  href='/blog'>return login page</a>"])

@route('/admin/data')
@route('/blog/admin/data')
def data():
    username = request.get_cookie("account", secret=secretkey)
    validuser=request.get_cookie("validuser", secret=secretkey)
    if username:
        if int(validuser) in listtoint(validadmin):
            return template('styles/'+styleadmin+'/template/data')
        return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["You do not have administrative powers"])
    return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["Please login username <br><a  href='/blog'>return login page</a>"])

@post('/admin/data')
@post('/blog/admin/data')
def edit_data():
    username=request.get_cookie("account", secret=secretkey)
    validuser=request.get_cookie("validuser", secret=secretkey)
    name= unicode(xsql(xss(request.forms.get('name'))), encoding='utf-8')
    blog= unicode(xsql(xss(request.forms.get('blog'))), encoding='utf-8')
    blogid= unicode(xsql(xss(request.forms.get('blogid'))), encoding='utf-8')
    comment= unicode(xsql(xss(request.forms.get('comment'))), encoding='utf-8')
    if username:
        if int(validuser) in listtoint(validadmin):
            if name:
                raw=infofetchall('username', name)
                if raw:
                    return ''''<META HTTP-EQUIV="Refresh" CONTENT="0;URL=/blog/admin/editusers/%d">'''%raw[0][0]
                return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["Username isn't correct"])
            elif blog:
                return '''<META HTTP-EQUIV="Refresh" CONTENT="0;URL=/blog/admin/blogedit/%d">'''%int(blog)
            elif blogid and comment:
                return '''<META HTTP-EQUIV="Refresh" CONTENT="0;URL=/blog/admin/commentedit?page=%d&id=%d">'''%(int(blogid), int(comment))
            else:
                return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["It's empty"])
        
@route('/admin/section')
@route('/blog/admin/section')
def admin_section():
    username = request.get_cookie("account", secret=secretkey)
    validuser=request.get_cookie("validuser", secret=secretkey)
    if username:
        if int(validuser) in listtoint(validadmin):
            return template('styles/'+styleadmin+'/template/section',sections=infosection())
        return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["You do not have administrative powers"])
    return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["Please login username <br><a  href='/blog'>return login page</a>"])
       
@post('/admin/section')
@post('/blog/admin/section')
def edit_section():
    username=request.get_cookie("account", secret=secretkey)
    validuser=request.get_cookie("validuser", secret=secretkey)
    section= unicode(xsql(xss(request.forms.get('section'))), encoding='utf-8')
    renamesection= unicode(xsql(xss(request.forms.get('renamesection'))), encoding='utf-8')
    rkeywords= unicode(xsql(xss(request.forms.get('rkeywords'))), encoding='utf-8')
    rdescription= unicode(xsql(xss(request.forms.get('rdescription'))), encoding='utf-8')
    box=request.forms.get('box')
    nsection= unicode(xsql(xss(request.forms.get('nsection'))), encoding='utf-8')
    keywords= unicode(xsql(xss(request.forms.get('keywords'))), encoding='utf-8')
    description= unicode(xsql(xss(request.forms.get('description'))), encoding='utf-8')
    if username:
        if int(validuser) in listtoint(validadmin):
            if renamesection and rkeywords and rdescription:
                editsection(renamesection,rkeywords,rdescription,  section)
                return template('styles/'+styleadmin+'/template/infoadmin',msg=lang['The new section has been saved'])
            elif box:
                deletesection(section)
                return template('styles/'+styleadmin+'/template/infoadmin',msg=lang['The section has been deleted'])
            elif nsection and keywords and description:
                newsection(nsection,keywords,description)
                return template('styles/'+styleadmin+'/template/infoadmin',msg=lang['The new section has been saved'])
            else:
                return template('styles/'+styleadmin+'/template/infoadmin',msg=lang['''It's empty'''])

@route('/admin/valid')
@route('/blog/admin/valid')
def admin_valid():
    username = request.get_cookie("account", secret=secretkey)
    validuser=request.get_cookie("validuser", secret=secretkey)
    if username:
        if int(validuser) in listtoint(validadmin):
            return template('styles/'+styleadmin+'/template/valid',infovalids=infovalids())
        return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["You do not have administrative powers"])
    return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["Please login username <br><a  href='/blog'>return login page</a>"])
     
@post('/admin/valid')
@post('/blog/admin/valid')
def edit_valid():
    global validblognew,validcommen,validadmin,valideditusers,validblogedit,validcommentedit
    username = request.get_cookie("account", secret=secretkey)
    validuser=request.get_cookie("validuser", secret=secretkey)
    validblognew= unicode(xsql(xss(request.forms.get('validblognew'))), encoding='utf-8')
    validcommen= unicode(xsql(xss(request.forms.get('validcommen'))), encoding='utf-8')
    validadmin= unicode(xsql(xss(request.forms.get('validadmin'))), encoding='utf-8')
    valideditusers= unicode(xsql(xss(request.forms.get('valideditusers'))), encoding='utf-8')
    validblogedit= unicode(xsql(xss(request.forms.get('validblogedit'))), encoding='utf-8')
    validcommentedit= unicode(xsql(xss(request.forms.get('validcommentedit'))), encoding='utf-8')
    if username:
        if int(validuser) in listtoint(validadmin):
            editvalid(validblognew,validcommen,validadmin,valideditusers,validblogedit,validcommentedit)
            return template('styles/'+styleadmin+'/template/infoadmin',msg=lang['The new permissions have been saved'])
        
@route('/admin/site')
@route('/blog/admin/site')
def admin_site():
    username = request.get_cookie("account", secret=secretkey)
    validuser=request.get_cookie("validuser", secret=secretkey)
    if username:
        if int(validuser) in listtoint(validadmin):
            return template('styles/'+styleadmin+'/template/site', site=infomysite)
        return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["You do not have administrative powers"])
    return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["Please login username <br><a  href='/blog'>return login page</a>"])

@post('/admin/site')
@post('/blog/admin/site')
def edit_site():
    global infomysite, modsite, modmsg
    username = request.get_cookie("account", secret=secretkey)
    validuser=request.get_cookie("validuser", secret=secretkey)
    title= unicode(xsql(xss(request.forms.get('title'))), encoding='utf-8')
    keywords= unicode(xsql(xss(request.forms.get('keywords'))), encoding='utf-8')
    description= unicode(xsql(xss(request.forms.get('description'))), encoding='utf-8')
    sitename= unicode(xsql(xss(request.forms.get('sitename'))), encoding='utf-8')
    siteurl= unicode(xsql(xss(request.forms.get('siteurl'))), encoding='utf-8')    
    modsite= int(xsql(request.forms.get('modsite')))
    modmsg= unicode(xsql(request.forms.get('modmsg')), encoding='utf-8')  
    if username:
        if int(validuser) in listtoint(validadmin):
            editsite(title,keywords,description,sitename,siteurl,modsite,modmsg)
            infomysite=infosite()
            modsite=infomysite[6]
            modmsg=infomysite[7]
            return template('styles/'+styleadmin+'/template/infoadmin',msg=lang['The new settings have been saved'])
              
@route('/admin/other')
@route('/blog/admin/other')
def admin_other():
    username = request.get_cookie("account", secret=secretkey)
    validuser=request.get_cookie("validuser", secret=secretkey)
    if username:
        if int(validuser) in listtoint(validadmin):
            return template('styles/'+styleadmin+'/template/other', other=infoother())
        return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["You do not have administrative powers"])
    return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["Please login username <br><a  href='/blog'>return login page</a>"])

@post('/admin/other')
@post('/blog/admin/other')
def edit_other():
    global cookie_age,waittime,sizeupload,numblog,numcomment, avatorwidth, avatorheight, style, lang
    username = request.get_cookie("account", secret=secretkey)
    validuser=request.get_cookie("validuser", secret=secretkey)
    cookie_age= xsql(xss(request.forms.get('cookie_age')))
    waittime= int(xsql(xss(request.forms.get('waittime'))))
    sizeupload= int(xsql(xss(request.forms.get('sizeupload'))))
    numblog= int(xsql(xss(request.forms.get('numblog'))))
    numcomment= int(xsql(xss(request.forms.get('numcomment'))))
    style= unicode(xsql(xss(request.forms.get('style'))), encoding='utf-8')
    styleadmin= unicode(xsql(xss(request.forms.get('styleadmin'))), encoding='utf-8')
    language= unicode(xsql(xss(request.forms.get('language'))), encoding='utf-8')
    avatorwidth= int(xsql(xss(request.forms.get('avatorwidth'))))
    avatorheight= int(xsql(xss(request.forms.get('avatorheight'))))
    try:
        exec('import languages.%s')%language
        exec('lang1=languages.%s.lang')%language
        lang=lang1
    except NameError:
        import languages.en
        lang=languages.en.lang
    if username:
        if int(validuser) in listtoint(validadmin):
            editother(cookie_age,waittime,sizeupload,numblog,numcomment,style,styleadmin,language, avatorwidth,avatorheight )
            return template('styles/'+styleadmin+'/template/infoadmin',msg=lang['The new settings have been saved'])

@route('/admin/userstable')
@route('/blog/admin/userstable')
def view_userstable():
    username=request.get_cookie("account", secret=secretkey)
    validuser=request.get_cookie("validuser", secret=secretkey)
    if username:
        if int(validuser) in listtoint(valideditusers):
            page = int(request.GET.get('page', '1'))
            if page==0: page=1
            next,back,end=page+1, page-1,10
            start= (page- 1) * end
            row=userstable(start, end)
            luser=lenuser()
            lend=luser/end
            return template('styles/'+styleadmin+'/template/users',row=row, back=back, next=next, page=page, luser=luser, lend=lend )
        return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["You do not have administrative powers"])
    return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["Please login username <br><a  href='/blog'>return login page</a>"])

@route('/admin/editusers/<id:int>')
@route('/blog/admin/editusers/<id:int>')
def edit_users(id):
    username=infousername=request.get_cookie("account", secret=secretkey)
    validuser=request.get_cookie("validuser", secret=secretkey)
    raw= infofetchall('id', id)
    if raw:
        if username:
            if int(validuser) in listtoint(valideditusers):
                return template('styles/'+styleadmin+'/template/edit_users', raw=raw[0])
            return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["You do not have administrative powers"])
        return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["Please login username <br><a  href='/blog'>return login page</a>"])
    return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["No user name is incorrect"])
 
@post('/admin/editusers/<id:int>')
@post('/blog/admin/editusers/<id:int>')
def save_userstable(id):
    username=request.get_cookie("account", secret=secretkey)
    validuser=request.get_cookie("validuser", secret=secretkey)
    name= unicode(xsql(xss(request.forms.get('name'))), encoding='utf-8')
    password= unicode(xsql(xss(request.forms.get('password'))), encoding='utf-8')
    email= unicode(xsql(xss(request.forms.get('email'))), encoding='utf-8')
    valid= int(xsql(xss(request.forms.get('valid'))))
    signature= unicode(xsql(xss(request.forms.get('signature'))), encoding='utf-8')
    if username:
        if int(validuser) in listtoint(valideditusers):
            infouser=infofetchall('id', id)[0]
            oldname=infouser[1]
            oldemail=infouser[3]
            infopicture=infouser[7]
            if oldname!=name:
                updateuser(name,oldname)
            if oldemail!=email:
                updateemail(email,oldemail)
            box= request.forms.get('box')
            if box:
                os.remove('avator/'+infopicture+'.jpeg')
                deleteuser(name)
                return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["The user has been deleted <br><a href='/blog/admin/userstable'>return userstable page</a>"])
            if password:
                salt=prandom()
                password=pssmd5(password,salt)
                editusers(password, valid, signature,salt,id)
            else:
                editusersnopass(valid, signature, id)
            return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["Data has been saved new user  <br><a href='/blog/admin/userstable'>return userstable page</a>"])
        return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["You do not have administrative powers"])
    return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["Please login username <br><a  href='/blog'>return login page</a>"])

@post('/admin/editusers/pic')
@post('/blog/admin/editusers/pic')
def usercp_pic():
    username= unicode(xsql(xss(request.forms.get('username'))), encoding='utf-8')
    infousername=request.get_cookie("account", secret=secretkey)
    validuser=request.get_cookie("validuser", secret=secretkey)
    if infousername:
        if int(validuser) in listtoint(valideditusers):
            try: # Windows needs stdio set for binary mode.
                from msvcrt import setmode
                setmode (0, os.O_BINARY) # stdin  = 0
                setmode (1, os.O_BINARY) # stdout = 1
            except ImportError:
                pass
            username=infofetchall('username', username)[0]
            idusername=username[0]
            infopicture=username[7]
            picture= request.files.get('picture')
            if picture !=None:
                raw = picture.file 
                filename = picture.filename.lower()
                if filename.endswith(('jpg', 'gif', 'png', 'bmp')):
                    end=filename[-3:]
                elif filename.endswith('jpeg'):
                    end=filename[-4:]
                else:
                    return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["Extension is allowed, permitted extensions (jpg, gif, png, bmp, jpeg)"])
                dirs=os.path.dirname(__file__)+'/avator/'
                avator=str(idusername)+'.'+end 
                logfile = file(dirs+avator, 'wb')
                for chunk in fbuffer(raw):
                    logfile.write(chunk)   
                logfile.close()
                sizefile=(int(os.path.getsize(dirs+avator))/1024)
                if sizefile>sizeupload:
                    os.remove(dirs+avator)
                    return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["Size is not allowed, you must be the size is less than 2 MB"])
                try:
                    import Image
                    imin = Image.open(dirs+avator)
                    imout = imin.resize((avatorwidth, avatorheight), Image.BICUBIC) 
                    os.remove('avator/'+avator)
                    avator=str(idusername)+'.jpeg'
                    imout.convert('RGB').save(dirs+avator)
                except ImportError:
                    if end!='jpeg':
                        os.remove('avator/'+avator)
                        return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["Extension is allowed, permitted extensions (jpeg)"])
                    else:
                        pass
                except NameError:
                    pass
                except  IOError:
                    os.remove('avator/'+avator)
                    return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["avator isn't correct"])
                return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["avator has been saved successfully"])
            return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["Did not choose a avator"])

@route('/admin/blogedit/<id:int>')
@route('/blog/admin/blogedit/<id:int>')
def edit_blog(id):
    username=request.get_cookie("account", secret=secretkey)
    validuser=request.get_cookie("validuser", secret=secretkey)
    blog=infoblog(id)
    if username:
        if int(validuser) in listtoint(validblogedit):
            if blog:
                return template('styles/'+styleadmin+'/template/edit_blog',blog=blog, sections=infosection())
            return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["ID error"])
        return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["You do not have administrative powers"])
    return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["Please login username <br><a  href='/blog'>return login page</a>"])

@post('/admin/blogedit/<id:int>')
@post('/blog/admin/blogedit/<id:int>')
def save_blog(id):
    username = request.get_cookie("account", secret=secretkey)
    validuser=request.get_cookie("validuser", secret=secretkey)
    title= unicode(xsql(xss(request.forms.get('title'))), encoding='utf-8')
    titletext= unicode(xsql(request.forms.get('titletext')), encoding='utf-8')
    section= unicode(xsql(xss(request.forms.get('section'))), encoding='utf-8')
    keywords= unicode(xsql(xss(request.forms.get('keywords'))), encoding='utf-8')
    description= unicode(xsql(xss(request.forms.get('description'))), encoding='utf-8')
    box= request.forms.get('box')
    if username:
        if int(validuser) in listtoint(validblogedit):
            if box:
                deleteblog(id)
                return '''<META HTTP-EQUIV="Refresh" CONTENT="0;URL=/blog/">'''
            if not keywords: keywords=''
            if not description: description=''
            editblog(title, titletext, section,keywords, description, id)
            return '''<META HTTP-EQUIV="Refresh" CONTENT="0;URL=/blog/comment/%s">'''%id

@route('/admin/commentedit')
@route('/blog/admin/commentedit')
def edit_comment():
    page = int(request.GET.get('page'))
    id = int(request.GET.get('id'))
    comment=infocomments(page)[id-1]
    username=request.get_cookie("account", secret=secretkey)
    validuser=request.get_cookie("validuser", secret=secretkey)
    if username:
        if int(validuser) in listtoint(validcommentedit):
            if comment:
                return template('styles/'+styleadmin+'/template/edit_comment', comment=comment)
                return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["ID error"])
        return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["You do not have administrative powers"])
    return template('styles/'+styleadmin+'/template/infoadmin',msg=lang["Please login username <br><a  href='/blog'>return login page</a>"])

@post('/admin/commentedit')
@post('/blog/admin/commentedit')
def save_comment():
    username = request.get_cookie("account", secret=secretkey)
    validuser=request.get_cookie("validuser", secret=secretkey)
    page = int(request.GET.get('page'))
    id= int(xsql(xss(request.forms.get('id'))))
    comment= unicode(xsql(request.forms.get('comment')), encoding='utf-8')
    box= request.forms.get('box')
    if username:
        if int(validuser) in listtoint(validcommentedit):
            if box:
                delblog2comm(page)
                deletecomment(id)
            editcomment(comment, id)
            return '''<META HTTP-EQUIV="Refresh" CONTENT="0;URL=/blog/comment/%s">'''%page

###########static
@route('/avator/:filename')
@route('/blog/avator/:filename')
def server_static(filename):
    return static_file(filename, root='./avator')  

@route('/editor/<filepath:path>')
@route('/blog/editor/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./editor')

@route('/styles/style/static_file/<filepath:path>')
@route('/blog/styles/style/static_file/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./styles/'+style+'/static_file')

@route('/styles/admin/static_file/<filepath:path>')
@route('/blog/styles/admin/static_file/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./styles/'+styleadmin+'/static_file')

###########run 
#debug(True)
if __name__ == "__main__":
    debug(True)
    run(reloader=True)
