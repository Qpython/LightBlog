#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import MySQLdb
import sys
import config
from functions import pssmd5, prandom

def sql():
    db = MySQLdb.connect(config.host, config.username,config.passdb , config.namedb, charset = "utf8", use_unicode = True)
    return db.cursor()

###########user
def newuser(username,password, email, ip,date,salt,valid=2,signature='The signature'):
    cursor=sql()
    cursor.execute("INSERT INTO users(username,password,email,ip,date,valid,signature,password2,salt) VALUES('%s', '%s' ,'%s','%s','%s',%d,'%s','%s','%s')"%(username,password, email, ip,date, valid,signature, password,salt))
    id=cursor.lastrowid
    cursor.execute(("UPDATE users SET avator='%s' WHERE id=%d")%(id, id))
    cursor.close()
    return id

def infoall(setsql, username):
    cursor=sql()
    row=cursor.execute(("SELECT * from users where %s='%s'")%(setsql, username))
    cursor.close() 
    return row
    
def infofetchall(setsql, username):
    cursor=sql()
    cursor.execute(("SELECT * from users where %s='%s'")%(setsql, username))
    row=cursor.fetchall()
    cursor.close() 
    return row
 
def userstable(start, end):
    cursor=sql()
    cursor.execute("SELECT * from users LIMIT %d,%d"%(start, end))
    row=cursor.fetchall()
    cursor.close() 
    return row
    
def editusers(password, valid, signature,salt,id):
    cursor=sql()
    cursor.execute(("UPDATE users SET password='%s',valid=%d ,signature='%s',password2='%s',salt='%s'  WHERE id=%d")%(password, valid, signature,password,salt,id))
    cursor.close() 
    
def updateuser(name,oldname):
    cursor=sql()
    cursor.execute(("UPDATE users SET username='%s'  WHERE username='%s'")%(name,oldname))
    cursor.execute(("UPDATE blog SET username='%s'  WHERE username='%s'")%(name,oldname))
    cursor.execute(("UPDATE comment SET username='%s'  WHERE username='%s'")%(name,oldname))
    cursor.close() 
    
def updateemail(email,oldemail):
    cursor=sql()
    cursor.execute(("UPDATE users SET email='%s'  WHERE email='%s'")%(email,oldemail))
    cursor.execute(("UPDATE comment SET email='%s'  WHERE email='%s'")%(email,oldemail))
    cursor.close() 
    
def editusercppass(password, email, signature, username, salt):
    cursor=sql()
    cursor.execute(("UPDATE users SET password='%s', email='%s',signature='%s',password2='%s',salt='%s' WHERE username='%s'")%(password, email, signature,password,salt,username))
    cursor.close() 
    
def editpass2(password2, email):
    cursor=sql()
    cursor.execute(("UPDATE users SET password2='%s'  WHERE email='%s'")%(password2, email))
    cursor.close() 
    
def editusercp(email, signature, username):
    cursor=sql()
    cursor.execute(("UPDATE users SET email='%s',signature='%s'  WHERE username='%s'")%( email, signature, username))
    cursor.close() 

def editusersnopass(valid, signature, id):
    cursor=sql()
    cursor.execute(("UPDATE users SET valid=%d,signature='%s' WHERE id=%d")%(valid, signature, id))
    cursor.close() 

def deleteuser(name):
    cursor=sql()
    cursor.execute(("delete from users where username='%s'")%name)
    cursor.execute(("delete from blog where username='%s'")%name)
    cursor.execute(("delete from comment where username='%s'")%name)
    cursor.close() 

def lenuser():
    cursor=sql()
    cursor.execute("SELECT * from users")
    row=cursor.rowcount
    cursor.close() 
    return row

############blog

def newblog(username,title,titletext,section,keywords, description,ip, date):
    cursor=sql()
    cursor.execute('''INSERT INTO blog(username,title,titletext,date,section,keywords, description,ip,comments) VALUES('%s', '%s' ,'%s','%s','%s','%s','%s','%s',0)'''%(username,title,titletext,date, section, keywords,description, ip ))
    row=cursor.lastrowid
    cursor.close()
    return row

def infoblog(id):
    cursor=sql()
    row=cursor.execute(("SELECT * from blog where id='%d'")%(id))
    row=cursor.fetchone()
    cursor.close() 
    return row
  
def infoblogall(start, end):
    cursor=sql()
    cursor.execute("SELECT * FROM blog ORDER BY Id  DESC LIMIT %d,%d"%(start, end))
    row=cursor.fetchall()
    cursor.close() 
    return row

def infoblogsection(section, start,end):
    cursor=sql()
    cursor.execute("SELECT * FROM blog where section='%s' ORDER BY Id  DESC LIMIT %d,%d"%(section, start, end))
    row=cursor.fetchall()
    cursor.close() 
    return row

def lenblog():
    cursor=sql()
    cursor.execute("SELECT * from blog")
    row=cursor.rowcount
    cursor.close() 
    return row
    
def lenblogsection(section):
    cursor=sql()
    cursor.execute("SELECT * from blog where section='%s'"%(section))
    row=cursor.rowcount
    cursor.close() 
    return row
  
def deleteblog(id):
    cursor=sql()
    cursor.execute(("delete from blog where id='%s'")%id)
    cursor.execute(("delete from comment where page='%s'")%id)
    cursor.close() 

def editblog(title, titletext, section,keywords, description, id):
    cursor=sql()
    cursor.execute(("UPDATE blog SET title='%s', titletext='%s',section='%s',keywords='%s',description='%s' WHERE id=%d")%(title, titletext, section,keywords, description, id))
    cursor.close() 

def infoblogip(ip):
    cursor=sql()
    row=cursor.execute(("SELECT * from blog where ip='%s' ORDER BY Id  DESC")%(ip))
    if row:
        row=cursor.fetchone()[4]
    cursor.close() 
    if row:
        return row

def infoblogmap():
    cursor=sql()
    row=cursor.execute("SELECT * from blog")
    row=cursor.fetchall()
    cursor.close() 
    return row
    
############comment

def newcomment(username,page,email,post,ip,avator,date):
    cursor=sql()
    cursor.execute('''INSERT INTO comment(username,page,email,post,date,ip,avator) VALUES('%s', '%d' ,'%s','%s','%s','%s','%s')'''%(username,page,email,post,date,ip,avator))
    row=cursor.lastrowid
    cursor.close()
    return row
    
def infocomments(page):
    cursor=sql()
    row=cursor.execute(("SELECT * from comment where page='%d' Order By id ASC")%(page))
    row=cursor.fetchall()
    cursor.close() 
    return row

def editcomment(comment, id):
    cursor=sql()
    cursor.execute(("UPDATE comment SET post='%s' WHERE id=%d")%(comment, id))
    cursor.close() 
    
def deletecomment(id):
    cursor=sql()
    cursor.execute(("delete from comment where id='%s'")%id)
    cursor.close() 

def infocommentall(show):
    cursor=sql()
    cursor.execute("SELECT * FROM comment ORDER BY Id  DESC LIMIT %d"%(show))
    row=cursor.fetchall()
    cursor.close() 
    return row

def infocommentip(ip):
    cursor=sql()
    row=cursor.execute(("SELECT * from comment where ip='%s' ORDER BY Id  DESC")%(ip))
    if row:
        row=cursor.fetchone()[5]
    cursor.close() 
    if row:
        return row

def addblog2comm(id):
    cursor=sql()
    cursor.execute(("UPDATE blog SET comments=comments+1 WHERE id=%d")%(id))
    cursor.close() 

def delblog2comm(id):
    cursor=sql()
    cursor.execute(("UPDATE blog SET comments=comments-1 WHERE id=%d")%(id))
    cursor.close() 
    
########section
def newsection(nsection,keywords,description):
    cursor=sql()
    cursor.execute('''INSERT INTO section(sectionname,keywords,description) VALUES('%s','%s','%s')'''%(nsection,keywords,description))
    cursor.close()

def editsection(newsection,keywords,description,  sectionname):
    cursor=sql()
    cursor.execute(("UPDATE section SET sectionname='%s',keywords='%s',description='%s' WHERE sectionname='%s'")%(newsection,keywords,description, sectionname))
    cursor.execute(("UPDATE blog SET section='%s' WHERE section='%s'")%(newsection,  sectionname))
    cursor.close() 
        
def deletesection(sectionname):
    cursor=sql()
    cursor.execute(("delete from section where sectionname='%s'")%sectionname)
    cursor.execute(("delete from blog where section='%s'")%sectionname)
    cursor.close()
    
def infosection():
    cursor=sql()
    row=cursor.execute("SELECT * from section")
    row=cursor.fetchall()
    cursor.close() 
    return row

def ifsection(sectionname):
    cursor=sql()
    row=cursor.execute(("SELECT * from section where sectionname='%s'")%(sectionname))
    row=cursor.fetchall()
    cursor.close() 
    return row

########valid
def infovalid(validname):
    cursor=sql()
    row=cursor.execute(("SELECT %s from valid")%(validname))
    row=cursor.fetchall()[0][0]
    cursor.close() 
    return row

def infovalids():
    cursor=sql()
    row=cursor.execute("SELECT * from valid")
    row=cursor.fetchall()[0]
    cursor.close() 
    return row

def editvalid(validblognew,validcommen,validadmin,valideditusers,validblogedit,validcommentedit):
    cursor=sql()
    cursor.execute(("UPDATE valid SET validblognew='%s',validcommen='%s',validadmin='%s',valideditusers='%s',validblogedit='%s',validcommentedit='%s' ")%(validblognew,validcommen,validadmin,valideditusers,validblogedit,validcommentedit))
    cursor.close() 
    
##############site
def infosite():
    cursor=sql()
    row=cursor.execute(("SELECT * from site"))
    row=cursor.fetchall()[0]
    cursor.close() 
    return row
    
def editsite(title,keywords,description,sitename,siteurl):
    cursor=sql()
    cursor.execute(("UPDATE site SET title='%s',keywords='%s',description='%s',sitename='%s',siteurl='%s' ")%(title,keywords,description,sitename,siteurl))
    cursor.close() 

##############other
def infoother():
    cursor=sql()
    row=cursor.execute(("SELECT * from other"))
    row=cursor.fetchall()[0]
    cursor.close() 
    return row

def editother(cookie_age,waittime,sizeupload,numblog,numcomment,style,styleadmin,language,avatorwidth,avatorheight):
    cursor=sql()
    cursor.execute(("UPDATE other SET cookie_age='%s',waittime='%d',sizeupload='%d',numblog='%d',numcomment='%d',style='%s',styleadmin='%s',language='%s',avatorwidth='%d',avatorheight='%d'")%(cookie_age,waittime,sizeupload,numblog,numcomment,style,styleadmin,language,avatorwidth,avatorheight))
    cursor.close() 
    
    
if __name__ == "__main__":
    password=raw_input('add new password admin:')
    email=raw_input('add new email admin:')
    salt=prandom()
    password=pssmd5(password,salt)
    cursor=sql()
    date=datetime.now().ctime()
    cursor.execute('CREATE TABLE users (Id INT PRIMARY KEY AUTO_INCREMENT, username VARCHAR(50), password VARCHAR(50), email VARCHAR(100), ip VARCHAR(20), date VARCHAR(100),valid INT,avator VARCHAR(20),signature TEXT,password2 VARCHAR(50),salt VARCHAR(6))DEFAULT CHARSET=utf8')
    cursor.execute('CREATE TABLE blog (Id INT PRIMARY KEY AUTO_INCREMENT, username VARCHAR(50), title VARCHAR(100), titletext TEXT, date VARCHAR(100),section VARCHAR(100),keywords TEXT,description TEXT,ip VARCHAR(20),comments INT)DEFAULT CHARSET=utf8')
    cursor.execute('CREATE TABLE comment (Id INT PRIMARY KEY AUTO_INCREMENT, username VARCHAR(50), page INT(10), email VARCHAR(100), post TEXT, date VARCHAR(100),ip VARCHAR(20),avator VARCHAR(20))DEFAULT CHARSET=utf8')
    cursor.execute('CREATE TABLE section (Id INT PRIMARY KEY AUTO_INCREMENT, sectionname VARCHAR(100),keywords TEXT,description TEXT)DEFAULT CHARSET=utf8')
    cursor.execute('CREATE TABLE valid (Id INT PRIMARY KEY AUTO_INCREMENT, validblognew TEXT,validcommen TEXT,validadmin TEXT,valideditusers TEXT,validblogedit TEXT,validcommentedit TEXT)DEFAULT CHARSET=utf8')
    cursor.execute('CREATE TABLE site (Id INT PRIMARY KEY AUTO_INCREMENT, title VARCHAR(100),keywords TEXT,description TEXT,sitename VARCHAR(100),siteurl VARCHAR(100))DEFAULT CHARSET=utf8')
    cursor.execute('CREATE TABLE other (Id INT PRIMARY KEY AUTO_INCREMENT, cookie_age VARCHAR(100),waittime INT,sizeupload INT,numblog INT,numcomment INT,style VARCHAR(100),styleadmin VARCHAR(100),language VARCHAR(100),avatorwidth INT,avatorheight INT)DEFAULT CHARSET=utf8')
    cursor.execute("INSERT INTO users(username,password,email,ip,date,valid,avator,signature,password2,salt) VALUES('admin', '%s' ,'%s','127.0.0.1','%s',1,'1','MY signature','%s','%s')"%(password,email, date, password, salt))
    cursor.execute("INSERT INTO blog(username,title,titletext,date,section,keywords,description,ip,comments) VALUES('admin', 'Hello!' ,'This is an example of a post.','%s','General','examle1,examle2,examle3','examle for description','127.0.0.1','0')"%date)
    cursor.execute("INSERT INTO comment(username,page,email,post,date,ip,avator) VALUES('admin', 1 ,'%s','This is an example of a comment.','%s','127.0.0.1','1')"%(email, date))
    cursor.execute("INSERT INTO section(sectionname,keywords,description) VALUES('General','keywords1,keywords2,keywords3','examle for description')")
    cursor.execute("INSERT INTO valid(validblognew,validcommen,validadmin,valideditusers,validblogedit,validcommentedit) VALUES('%s','%s','%s','%s','%s','%s')"%('1,2', '', '1', '1', '1','1'))
    cursor.execute("INSERT INTO  site(title,keywords,description,sitename,siteurl) VALUES('%s','%s','%s','%s','%s')"%('LightBlog', 'blog,Easy,simple,python,LightBlog'
    , 'simple Blog in Python language and Easy development Because it uses a bottle framework.', 'mysyte', 'www.site.com'))
    cursor.execute("INSERT INTO other (cookie_age,waittime,sizeupload,numblog,numcomment,style,styleadmin,language,avatorwidth,avatorheight) VALUES('9000',10,2097152,10,10,'default','admin','en',100,100)")
    cursor.close()
    raw_input('Been completed successfully create the database,Press the enter for exit.')

