from bs4 import BeautifulSoup
import requests


gpu = input("What product dp i wamt to search for? ")

url = f"https://www.newegg.com/p/pl?d={gpu}"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")


page_text = doc.find(class_="list-tool-pagination-text")
print(page_text)