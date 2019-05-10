import time
from selenium import webdriver
import sys
import urllib.request
# import requests
# from PIL import Image
# from io import BytesIO

# Pass search query while running script from command  -- >> python download_img.py cars

url = "https://unsplash.com/search/photos/" + sys.argv[1] if len(sys.argv) > 1 else "https://unsplash.com"
driver = webdriver.Chrome('/Users/navpreetsingh/Downloads/chromedriver')
driver.maximize_window()
driver.get(url);

driver.execute_script("window.scrollTo(0,1000);")
time.sleep(3)

image_elements = driver.find_elements_by_css_selector("#gridMulti img")  # Finding elements with img tag in multi grid

i = 1
for image_element in image_elements:
    image_url = image_element.get_attribute("src")
    print("Image URL number ", i ," = ",image_url)
    urllib.request.urlretrieve(image_url,"downloaded_image_(%d).jpg" %i)      # Saving file from URL
    i = i+1

    # To limit download limit to a specific number
    if i > 5:
        print("Limit is set to download number of images")
        break

print("Images have been downloaded")
driver.quit()