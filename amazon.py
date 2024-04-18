import requests
from bs4 import BeautifulSoup
import csv



url=''

response=requests.get(url)
print(response.status_code)