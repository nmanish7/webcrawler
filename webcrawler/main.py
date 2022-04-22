from pathlib import Path
import requests
import urllib.request as urllib2
from termcolor import cprint
from bs4 import BeautifulSoup
from lxml import html

# cprint("this is manish", "red")

pagination_input = 5
google_search_engine = "https://www.google.com/search?q="
keyword = "love"
pagination_number = 0

exit()
pagination = "start="
url = f"{google_search_engine}{keyword}&{pagination}{pagination_number}"
user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
headers = {'User-Agent': user_agent}

request = urllib2.Request(url, None, headers)

html = urllib2.urlopen(request).read()


soup = BeautifulSoup(html, "html.parser")

selector = soup.find_all('cite')

links = [next(item.children) for item in selector]

links = set(links)
print(links)

# selector = selector.children

# print(next(selector))

# first = "https://www.google.com/search?q=love&source=hp&ei=1n9hYpvqNJOj1e8P6ZuBwAk&iflsig=AHkkrS4AAAAAYmGN5lkSvpJDc4YzNuN8eQ-rKe-myPic&ved=0ahUKEwibrbHHw6X3AhWTUfUHHelNAJgQ4dUDCAc&uact=5&oq=love&gs_lcp=Cgdnd3Mtd2l6EAMyCwgAEIAEELEDEIMBMggIABCABBCxAzIICAAQgAQQsQMyCAguEIAEELEDMgsILhCABBCxAxCDATILCC4QgAQQsQMQ1AIyCwguEIAEELEDENQCMggIABCABBCxAzIICAAQgAQQsQMyBQguEIAEOgUIABCABDoICAAQsQMQgwFQAFiRBGDLBWgAcAB4AIAB2wGIAbsEkgEFMC4yLjGYAQCgAQE&sclient=gws-wiz"
# second = "https://www.google.com/search?q=love&ei=2H9hYqeyOeSeseMPqKmO4Ag&start=10&sa=N&ved=2ahUKEwin_q_Iw6X3AhVkT2wGHaiUA4wQ8tMDegQIAhA4&biw=770&bih=712&dpr=1.25"
