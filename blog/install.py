#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import MySQLdb
import sys
import config
from functions import pssmd5, prandom
import config
import model

if __name__ == "__main__":
    password=raw_input('add new password admin:')
    email=raw_input('add new email admin:')
    salt=prandom()
    password=pssmd5(password,salt)
    cursor=model.sql()
    date=datetime.now().ctime()
    cursor.execute('CREATE TABLE users (Id INT PRIMARY KEY AUTO_INCREMENT, username VARCHAR(50), password VARCHAR(50), email VARCHAR(100), ip VARCHAR(20), date VARCHAR(100),valid INT,avator VARCHAR(20),signature TEXT,password2 VARCHAR(50),salt VARCHAR(6))DEFAULT CHARSET=utf8')
    cursor.execute('CREATE TABLE blog (Id INT PRIMARY KEY AUTO_INCREMENT, username VARCHAR(50), title VARCHAR(100), titletext TEXT, date VARCHAR(100),section VARCHAR(100),keywords TEXT,description TEXT,ip VARCHAR(20),comments INT)DEFAULT CHARSET=utf8')
    cursor.execute('CREATE TABLE comment (Id INT PRIMARY KEY AUTO_INCREMENT, username VARCHAR(50), page INT(10), email VARCHAR(100), post TEXT, date VARCHAR(100),ip VARCHAR(20),avator VARCHAR(20))DEFAULT CHARSET=utf8')
    cursor.execute('CREATE TABLE section (Id INT PRIMARY KEY AUTO_INCREMENT, sectionname VARCHAR(100),keywords TEXT,description TEXT)DEFAULT CHARSET=utf8')
    cursor.execute('CREATE TABLE valid (Id INT PRIMARY KEY AUTO_INCREMENT, validblognew TEXT,validcommen TEXT,validadmin TEXT,valideditusers TEXT,validblogedit TEXT,validcommentedit TEXT)DEFAULT CHARSET=utf8')
    cursor.execute('CREATE TABLE site (Id INT PRIMARY KEY AUTO_INCREMENT, title VARCHAR(100),keywords TEXT,description TEXT,sitename VARCHAR(100),siteurl VARCHAR(100),modsite INT,modmsg text)DEFAULT CHARSET=utf8')
    cursor.execute('CREATE TABLE other (Id INT PRIMARY KEY AUTO_INCREMENT, cookie_age VARCHAR(100),waittime INT,sizeupload INT,numblog INT,numcomment INT,style VARCHAR(100),styleadmin VARCHAR(100),language VARCHAR(100),avatorwidth INT,avatorheight INT)DEFAULT CHARSET=utf8')
    cursor.execute("INSERT INTO users(username,password,email,ip,date,valid,avator,signature,password2,salt) VALUES('admin', '%s' ,'%s','127.0.0.1','%s',1,'1','MY signature','%s','%s')"%(password,email, date, password, salt))
    cursor.execute("INSERT INTO blog(username,title,titletext,date,section,keywords,description,ip,comments) VALUES('admin', 'Hello!' ,'This is an example of a post.','%s','General','examle1,examle2,examle3','examle for description','127.0.0.1','0')"%date)
    cursor.execute("INSERT INTO comment(username,page,email,post,date,ip,avator) VALUES('admin', 1 ,'%s','This is an example of a comment.','%s','127.0.0.1','1')"%(email, date))
    cursor.execute("INSERT INTO section(sectionname,keywords,description) VALUES('General','keywords1,keywords2,keywords3','examle for description')")
    cursor.execute("INSERT INTO valid(validblognew,validcommen,validadmin,valideditusers,validblogedit,validcommentedit) VALUES('%s','%s','%s','%s','%s','%s')"%('1,2', '', '1', '1', '1','1'))
    cursor.execute("INSERT INTO  site(title,keywords,description,sitename,siteurl,modsite,modmsg) VALUES('%s','%s','%s','%s','%s',1,'')"%('LightBlog', 'blog,Easy,simple,python,LightBlog'
    , 'simple Blog in Python language and Easy development Because it uses a bottle framework.', 'mysyte', 'www.site.com'))
    cursor.execute("INSERT INTO other (cookie_age,waittime,sizeupload,numblog,numcomment,style,styleadmin,language,avatorwidth,avatorheight) VALUES('9000',10,2097152,10,10,'default','admin','en',100,100)")
    cursor.close()
    raw_input('Been completed successfully create the database,Press the enter for exit.')
