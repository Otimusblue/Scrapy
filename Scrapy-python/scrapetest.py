from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

#SIMPLEST SCRAPING

html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
# print(html)
# res = re.findall(r"<title>(.+?)</title>", html)
# print("\nPage title is: ", res[0])


#ALL PARAGRAPH
# res = re.findall(r"<p>(.*?)</p>", html, flags=re.DOTALL)    # re.DOTALL if multi line
# print("\nPage paragraph is: ", res[0])

#ALL LINK
res = re.findall(r'href="(.*?)"', html)
print("\nAll links: ", res[0])


#The .+? form requires at least one character to match

#  html = urlopen("http://www.pythonscraping.com/pages/page3.html")
# html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
# bsObj = BeautifulSoup(html)
#nameList = bsObj.findAll("span",{"class":"green"})
# for name in nameList:
#     print(name.get_text())

#FIND WITH CONTENT

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

# images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
# for image in images:
#  print(image["src"])



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

#SIMPLEST SCRAPING




