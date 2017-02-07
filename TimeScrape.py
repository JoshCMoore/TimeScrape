from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup
import re
import os

html = urlopen("http://www.nytimes.com/pages/todayspaper/index.html")
bsObj = BeautifulSoup(html, "html.parser")
temp = bsObj.find("div", {"class":"abColumn"})
#print(temp.parent)
list = []
count =0

for link in temp.findAll("a",href=re.compile("^(http://www.nytimes.com/)[0-9]{4}")):
    if 'href' in link.attrs:
       #print(link.attrs['href'])
       if(link.attrs['href']) not in list:
            list.append(link.attrs['href'])

size = 0
folder=input("What is your destination folder?")
for link in list:
    print(link)
    html = urllib.request.build_opener(urllib.request.HTTPCookieProcessor).open(link)
    bsObj = BeautifulSoup(html,"html.parser")
    title = str(bsObj.find("title").get_text())
    fileName=folder+"\\"+title+".txt"
    while(fileName.__contains__("?")):
        fileName=fileName.replace("?","")
    f = open(fileName,'w')
    string = ""
    for x in bsObj.findAll("p", {"class" : "story-body-text story-content" }):
        string+=x.getText()
    f.write(string)
    f.close()
print("done")
