#importing modules
import requests
from bs4 import BeautifulSoup
import csv
import pandas as p
import datetime


# Get current date and time
now=datetime.datetime.now()

# Format date and time as needed
dateStr=now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Date and time:{dateStr}")

#scraping the data
url="https://www.flipkart.com/search?q=mobilies"
r=requests.get(url)

soup=BeautifulSoup(r.content,"html.parser")

titles=soup.find_all('div',class_="_4rR01T")
ratings=soup.find_all('div',class_="_3LWZlK")
reviews=soup.find_all('span',class_="_2_R_DZ")
prices=soup.find_all('div',class_="_25b18c")
links=soup.find_all('a',class_="ge-49M")

mt=[]
mr=[]
mre=[]
mp=[]
ml=[]

for titles,ratings,rev,pri,links in zip(titles,ratings,reviews,prices,links):
    mt.append(titles.text)
    mr.append(ratings.text)
    mre.append(rev.text)
    mp.append(pri.text)
    ml.append(links.text)

#saving data in csv
d={'mt':mt,'mr':mr,'mre':mre,'mp':mp,'ml':ml}
model=p.DataFrame(data=d)

model.to_csv("mobilesdata.csv")



