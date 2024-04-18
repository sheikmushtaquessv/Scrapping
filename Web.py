import requests
from bs4 import BeautifulSoup
import csv

#How to Extract Data from website
url="https://www.bikewale.com/royalenfield-bikes/"
page=requests.get(url)

soup=BeautifulSoup(page.content,'html.parser')

#images
image=soup.findAll('div',class_="o-brXWGL o-frwuxB")
for i in image:
    j=i.img['src']
    print(j)