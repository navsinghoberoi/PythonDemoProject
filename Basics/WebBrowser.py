import webbrowser

# Open frequently used URL's in browser

# webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
# webbrowser.open("https://automatetheboringstuff.com/")
# webbrowser.open("https://www.youtube.com/")
# webbrowser.open("https://www.primevideo.com/")
# webbrowser.open("https://www.netflix.com/browse")
# webbrowser.open("http://pythontutor.com/visualize.html#mode=display")



# #  Print all links from a website
# import bs4
# from urllib.request import Request, urlopen
# import re
#
# req = Request("http://slashdot.org")
# html_page = urlopen(req)
#
# soup = BeautifulSoup(html_page, "lxml")
#
# links = []
# for link in soup.findAll('a'):
#     links.append(link.get('href'))
#
# print(links)

# Print html of page
import urllib.request
html = urllib.request.urlopen("http://www.google.com/")       # source code of url
print(html.read())



# Post request
import urllib.parse
url = "https://pythonprogramming.net/"
values = {'s':'basic','submit' : 'Search'}
data = urllib.parse.urlencode(values)
data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)