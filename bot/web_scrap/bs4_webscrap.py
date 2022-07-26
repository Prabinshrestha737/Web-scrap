from unittest import result
from bs4 import BeautifulSoup

import requests

# with open("index.html", "r") as f:
#     doc = BeautifulSoup(f, "html.parser")


# print(doc)
# print(doc.prettify())


# tag = doc.title
# print(tag)
# print(tag.string)


#change string in tag variable

# tag.string = "Hello"
# print(tag)

# print(doc)

# tags = doc.find_all("p")[0]
# inside_tag = tags.find_all('b')


url = "https://www.newegg.com/p/1DW-00GP-00392?Description=1060%20ti&cm_re=1060_ti-_-9SIAC85HD45687-_-Product"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
# print(doc.prettify())

prices = doc.find(text="$")

parent = prices.parent
strong = parent.find("strong")
print(strong.string)

