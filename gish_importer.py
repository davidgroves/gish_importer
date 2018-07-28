#!/usr/bin/env python3

from bs4 import BeautifulSoup

# Went and copy+pasted list.php into list.html, so this can load it.
with open("list.html", encoding="utf8") as f:
    data = f.read()

soup = BeautifulSoup(data, 'html.parser')

descriptions = soup.findAll('div', attrs={'class': 'item-description'})
item_numbers = soup.findAll('span', attrs={'class': 'item-number'})
points = soup.findAll('span', attrs={'class': 'item-points ml-4'})
subtypes = soup.findAll('img', attrs={'class': 'item-status'})

for description, item_number, subtype, point in zip(descriptions, item_numbers, subtypes, points):

    output = []
    output.append(item_number.text)
    output.append(point.text.replace(" POINTS", "").strip())
    if subtype.get("src") == "assets/images/item-icons/video.png":
        output.append("video")
    if subtype.get("src") == "assets/images/item-icons/image.png":
        output.append("photo")
    if subtype.get("src") == "assets/images/item-icons/video-image.png":
        output.append("both")

    output.append(description.text.strip().replace('\n', ';'))

    for i in output:
        print('"' + i, end='",')
    print("")
