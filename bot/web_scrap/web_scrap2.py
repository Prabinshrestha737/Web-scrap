from bs4 import BeautifulSoup

with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")


# tag = doc.find("option")
# tag["value"] = "new val"
# print(tag)
# print(tag.attrs) #Gives all attributes 
# tag["selected"] = "false"
# tag["color"] = "blue"
# print(tag)

#find multiple tags 

# tag = doc.find(["p", "div", "li"])
# print(tag)


# tag = doc.find_all(["option"], text="Undergraduate")
# print(tag)

#Searching class name
# tag = doc.find_all(class_="btn-item")
# print(tag)

import re

#regular expression with limitations 
# tags = doc.find_all(text=re.compile("\$.*"), limit=1)

# for tag in tags:
#     print(tag.strip())


tags = doc.find_all("input", type="text")
for tag in tags:
    tag['placeholder'] = "I changed yoy!"

with open("changed.html", "w") as file:
    file.write(str(doc))

