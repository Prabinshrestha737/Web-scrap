from bs4 import BeautifulSoup


with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")


# print(doc)
# print(doc.prettify())


tag = doc.title
print(tag)
print(tag.string)


#change string in tag variable

# tag.string = "Hello"
# print(tag)

# print(doc)


tags = doc.find_all("p")[0]
inside_tag = tags.find_all('b')





