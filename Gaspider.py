#!/usr/bin/python2.7
import urllib
from bs4 import BeautifulSoup
#import difflib
import filecmp
import sys
import os
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

h = getHtml("http://www.dy2018.com/i/97374.html")

soup = BeautifulSoup(h)

#urls = soup.select("tbody tr td a")
urls = soup.find_all(href=re.compile("ftp"))


txt =  ''.join(map(str,urls))

#print txt
f = open('new.txt','w')
f.write(txt)
f.close()

res = filecmp.cmp('new.txt','old.txt')
if res != True:
	os.system('cp new.txt old.txt')
	os.system('./mail.sh')
