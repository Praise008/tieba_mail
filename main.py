#-*- coding:utf-8 -*-
import re
import sys
import requests
from bs4 import BeautifulSoup
#pn="?pn="
tieba_url="http://tieba.baidu.com/p/5638802871"
headers={
    "Host":"tieba.baidu.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
}
response = requests.get(tieba_url,headers=headers)
#soup=BeautifulSoup(response.content,"lxml")
#html=open("haha.html","r")
re_pages=r"\?pn=\d+"
re_mail=r"([0-9a-zA-Z_]+@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3})" #邮箱正则
re_search_mail=re.compile(re_mail)
re_search_pages=re.compile(re_pages)
repeat_page=re_search_pages.findall(response.content)
all_page=[]
all_mail=[]
for page in repeat_page:
    if page not in all_page:
        all_page.append(page)
#xx=open("haha.html","w").write(response.content)
one_page_mail=re_search_mail.findall(response.content)
all_mail+=one_page_mail
for page_url in all_page:
    print tieba_url+page_url
    page_response=requests.get(tieba_url+page_url,headers=headers)
    one_page_mail=re_search_mail.findall(page_response.content)
    all_mail+=one_page_mail
print all_mail

#if __name__=="__main__":
#    main()
