import requests
from bs4 import BeautifulSoup
import requests
import random

ARTIST_CLASS = "c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only"

# 2. Create an input() prompt that asks what year you would like to travel to in YYY-MM-DD format. e.g.


# 2. Using what you've learnt about BeautifulSoup, scrape the top 100 song titles on that date into a Python List.

# Hint: Take a look at the URL of the chart on a historical date: https://www.billboard.com/charts/hot-100/2000-08-12

# date_input = input("Enter the time you would like to travel to in YYYY-MM-DD format : ")

# (year, month, date) = (date_input.split(sep="-")[i] for i in range(3))

# creating soup
content = requests.get(url="https://www.billboard.com/charts/hot-100/")
content = content.text
soup = BeautifulSoup(content, "html.parser")

# digging for the div elements
class_name = "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"

divs = soup.findAll(name="div", class_="o-chart-results-list-row-container")
# finding the #1
number1_class = "c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet"
print(len(divs))
# todo get the no1 title

# no1=divs[0]

# number1_song=no1.select_one(selector="h3").text
# TODO get the 2-100 titles
for div in divs[0:1]:
    # print(div)
    # digging in the div soup
    headers = div.findAll(name="h3", )
    for header in headers:
        print(header.text)
        pass

# todo getting the artist names
for div in divs[1:1]:
    print(div)


# todo find no1
# todo find artist names
# using python type hints
def print_name(name: str) -> int:
    if name:
        return 1
    else:
        return 0


print(print_name(False))
from typing import Optional


def print_int(int1: int, int2: Optional[int]):
    print(str(int1) + " " + str(int2))


print_int(2, None)

# todo parsing using xpaths
from lxml import etree

# convert soup to a string
content = str(soup)
# create a tree
tree = etree.HTML(content)
# printing the tree
tree_str = etree.tostring(tree, pretty_print=True, method="HTML").decode()
# print(tree_str)
print("\n\n\n\n\n heey")
# getting the divs in the string
# getting the spans in the div that class contains c-label
new_divs = tree.xpath("//h3[contains(@class,'a-no-trucate')]")
# sieving to remove non songs
# sieved_divs=new_divs.xpath("//h3[contains(@class,'a-no-trucate')]")
# print(etree.tostring(new_divs,pretty_print=True,method="HTML").decode())

# print(etree.tostring(new_divs[0], pretty_print=True, method="HTML").decode())
# todo get the song titles
i = 1
song_list = [-1]
for div in new_divs:
    # fetch the string
    # div_string = etree.tostring(div, pretty_print=True, method="HTML").decode()

    # print(div.text)
    song_list.append(div.text)
    pass

# todo get the artist names
# print the entire tree
# print(etree.tostring(tree,pretty_print=True,method="HTML").decode())
# select the span inside the div ,the span contains c label in the class
artist_tree = tree.xpath("//span[contains(@class,'a-no-trucate')]")
i = 1
for x in artist_tree:
    print(i)
    # print("pppp")
    print(x.text)
    print(song_list[i])
    i += 1
    pass
# artist_tree=tree.xpath("")
