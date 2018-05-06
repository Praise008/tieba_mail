#-*- coding:utf-8 -*-
import re
import sys
import requests
from bs4 import BeautifulSoup
pn="?pn="
tieba_url="http://tieba.baidu.com/p/5638802871"
headers={
    "Host":"tieba.baidu.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
}
response = requests.get(tieba_url,headers=headers)
#soup=BeautifulSoup(response.content,"lxml")
re_mail=r"([0-9a-zA-Z_]+@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3})"
r=re.compile(re_mail)
#xx=open("haha.html","w").write(response.content)
all_mail=r.findall(response.content)
print all_mail
