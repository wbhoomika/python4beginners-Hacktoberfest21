from os import close
from re import S
import requests
from bs4 import BeautifulSoup


url="https://agomoni.org/"
data=requests.get(url)

htmlContent=data.content
#print(htmlContent)

soup=BeautifulSoup(htmlContent,'html.parser')
#print(soup.prettify)

#print(type(soup.title))
paras=soup.find_all('p')

#for para in paras:
#   print("Scrapped Text : ",para.get_text())

#body=soup.find('div',class_="content_wrap")
#for i in body.parents:
#    print(i)
#exit()



s=[]
anchors=soup.find_all('a')

for i in anchors:
    link=i.get('href')
    
    try:
        if(link!='#' and link[0:4]=='http'):
            s.append(link)
            print(link)
    except TypeError:
        pass


with open ('link.txt','w') as fs:
    for i in s:
        fs.write(f"{i}\n")
    fs.close()