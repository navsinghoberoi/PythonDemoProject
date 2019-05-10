import time

from selenium import webdriver

driver = webdriver.Chrome('/Users/navpreetsingh/Downloads/chromedriver')

url1 = "http://medium.com"
driver.execute_script('''window.open("_blank");''')       # Open a new tab
time.sleep(3)

i=1
driver.switch_to.window(driver.window_handles[i])
driver.get("https://www.youtube.com/")
time.sleep(3)


driver.quit()