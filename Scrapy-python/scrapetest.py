from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
#html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)
#nameList = bsObj.findAll("span",{"class":"green"})
# for name in nameList:
#     print(name.get_text())

# Find With Content

# nameList = bsObj.findAll(text="the prince")
# print(len(nameList))
# allText = bsObj.findAll(id="text")
# print(allText[0].get_text())

#CHILDREN

# for child in bsObj.find("table",{"id":"giftList"}).children:
#     print(child)


#SIBLINGS

# for child in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
#     print(child)

#DEALING WITH YOUR PARENT

# print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

#REGULAR EXPRESSIONS

images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
 print(image["src"])



# def getTitle(url):
#     try:
#         html = urlopen(url)
#     except HTTPError as e:
#         return None
#     try:
#         bsObj = BeautifulSoup(html.read())
#         title = bsObj.body.h1
#     except AttributeError as e:
#         return None
#     return title
# title = getTitle("http://pythonscraping.com/pages/page1.html")
# if title == None:
#     print("Title could not be found")
# else:
#     print(title)



