"""Script to print all the links on basis of search parameter from URL
While running this script, pass URL of website (1st param) and search query (2nd param)
NOTE - Length of arguments is 1 even if user does not enters any argument

If no params are provided , then result are displayed for medium website with python search param

Refer examples below --
https://medium.freecodecamp.org/search?q=searchParam
https://medium.com/search?q=searchParam
https://hackernoon.com/search?q=searchParam
https://en.wikipedia.org/wiki/searchParam

NOTE : Sample usage of this script-
a) python3 FindAndReadBlogs.py  https://medium.com java
b) python3 FindAndReadBlogs.py  https://medium.com
"""


import time
from selenium import webdriver
import sys

blogsMaxLimit = 3

print("Length of arguments entered by user while running script = ", len(sys.argv))

if len(sys.argv) > 2:
    url = sys.argv[1]               # 1st input taken while running script
    search_param = sys.argv[2]       # 2nd input taken while running script
    complete_url = str(url) + str("/search?q=" +search_param)
else:
    complete_url = "https://medium.com/search?q=python"


driver = webdriver.Chrome('/Users/navpreetsingh/Downloads/chromedriver')
# driver.maximize_window()
driver.get(complete_url);

if len(sys.argv) > 2:
    links_of_variable = "-" + str(search_param) + "-"
else:
    links_of_variable = "-python-"

blog_elements = driver.find_elements_by_tag_name("a")
print("Printing all links containing the keyword", links_of_variable)

final_url_list = []

i = 0

for elements in blog_elements:
    final_url = elements.get_attribute("href")
    if (links_of_variable in final_url) and (final_url not in final_url_list):
        final_url_list = final_url_list + [final_url]
        print(final_url)
        i = i+1

print("Total links printed = ", i)
print("List containing URLS = ", final_url_list)

# Open tabs of all links in new tabs
j=1
for j in range(1, len(final_url_list)):
    tab_url = final_url_list[j]
    driver.execute_script('''window.open("_blank");''')  # Open a new tab
    driver.switch_to.window(driver.window_handles[j])
    driver.get(tab_url)
    time.sleep(1)
    j = j+1

    # To limit opening tabs to 10
    if j >= blogsMaxLimit:
        print("LIMIT REACHED, not opening more tabs now")
        break


# Adding wait time before closing browser
time.sleep(5)
driver.quit()      #comment this line if you wanna read blogs
