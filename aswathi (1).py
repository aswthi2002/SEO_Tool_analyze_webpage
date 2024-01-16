import sqlite3
import smtplib
import re
import random
a=sqlite3.connect("ana.db")
#a.execute('create table ana(id int unique,username varchar(100),password varchar(100),email varchar(100),phone varchar(11))')
#a.execute('insert into ana(id,username,password,email,phone) values(1,"aswathi","1212","aswathilakshmi02@gmail.com","aswathi2002")')
#a.execute('drop table ana')
def create():
    id=int(input('Id:'))
    user=input('User:')
    email=input('Email:')
    phone=input('Phone:')
    pa1=[v for v in range(10)]
    pa2=[chr(v) for v in range(ord('a'),ord('z')+1)]
    pa3=[chr(v) for v in range(ord('A'),ord('Z')+1)] 
    pa4=['@','&','#']
    pas=""
    for i  in range(2):
        pas=pas+str(random.choice(pa1))
        pas=pas+str(random.choice(pa2))
        pas=pas+str(random.choice(pa3))
        pas=pas+str(random.choice(pa4))
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("aswathilakshmi02@gmail.com","uuzt atza fkcz fqow")
    msg1='username-'+str(user)+'/nYour Password is - '+str(pas)
    server.sendmail("aswathilakshmi02@gmail.com",email,msg1)
    print("Email received")
    a.execute('insert into ana(id,username,password,email,phone) values(?,?,?,?,?)',(id,user,pas,email,phone))
def login():
    user=input('enter username: ')
    pas=input('enter password: ')
    c=0
    d=a.execute('select * from ana where username=? and password=?',(user,pas))
    for c in d:
        print(c)
    if c!=0:
        print("login successful")
        while 1:
            import urllib.request
            ab='https://'+input("url")
            bc=urllib.request.urlopen(ab)
            import bs4
            cd=bs4.BeautifulSoup(bc,"html.parser")
            for de in cd(["style","script"]):
                de.extract()
            ef=cd.get_text()
            de=ef.split(" ")
            pp=open("ana.txt","r").read().split(" ")
            dic={}
            for cd in de:
                if cd not in pp:
                   dic[cd]=de.count(cd)
            sort=sorted(dic.items(),key=lambda t:t[1],reverse=True)
            print(sort[0:5])
            ab,bc=zip(*sort[0:5])
            import xlsxwriter
            ze=xlsxwriter.Workbook("ana.xlsx")
            y=ze.add_worksheet("chart")
            y.write(0,0,"words")
            y.write(0,1,"count")
            row=1
            col=0
            for k in range(5):
                y.write(row,col,ab[k])
                y.write(row,col+1,bc[k])
                row+=1
            chart=ze.add_chart({"type":"column"})
            chart.add_series({"categories":"=chart!A2:A6","values":"=chart!B2:B6"})
            y.insert_chart("D2",chart)
            ze.close()
            import os
            os.system("start ana.xlsx")
            sx=input("do you want to continue?")
            if sx.lower()=="yes":
                continue
            else:
                break
    else:
        print("login failed")
def change():
    id=int(input('enter id: '))
    x=input('1.username or 2. password: ')
    d=a.execute('select * from ana where id=? ',([id]))
    for c in d:
        pass
    email=c[3]
    if(x=='1'or x=="username"):
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login("aswathilakshmi02@gmail.com","uuzt atza fkcz fqow")
        y=[g for g in range (1000,9999)]
        r=random.choice(y)
        msg='OTP - '+str(r)
        server.sendmail("aswathilakshmi02@gmail.com",email,msg)
        ze=input("enter the generated OTP: ")    
        if ze==str(r):
            user=input("enter new username: ")
            a.execute('update ana set username=? where id=?',(user,id))
        else:
            print("OTP not matched")        
    elif(x=='2'or x=="password"):
        d=a.execute('select * from ana where id=? and phone=? ',([id,phone]))
        for c in d:
            pass
        email=c[3]
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login("aswathilakshmi02@gmail.com","uuzt atza fkcz fqow")
        y=[g for g in range (1000,9999)]
        r=random.choice(y)
        msg='OTP - '+str(r)
        server.sendmail("aswathilakshmi02@gmail.com",email,msg)
        ze=input("enter the generated OTP- ")
        if(ze==str(r)):
            pas=input("enter new password: ")
            a.execute('update ana set password=? where id=?',(pas,id))
        else:
            print("OTP not matched")
z=input('1.create /2.login /3.change')
if(z=='1'or z=="create"):
    create()
elif(z=='2'or z=="login"):
    login()
elif(z=='3'or z=="change"):
    change()
a.commit()
b=a.execute("select * from ana")
for h in b:
     print(h[0],h[1],h[3])
a.close()

















